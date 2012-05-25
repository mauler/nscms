#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime
from operator import attrgetter
import os

from django.core.files.storage import default_storage
from django.template.defaultfilters import slugify


def slugify_filename(filename):
    name, ext = os.path.splitext(filename)
    return slugify(name) + ext


class UploadTo(object):
    def __init__(self, base="portal", strftime="%Y/%m", instance_field="title", max_length=None):
        self.base = base
        self.strftime = strftime
        self.instance_field = instance_field
        self.max_length = max_length

    def __call__(self, instance, filename):
        Model = type(instance)
        max_length = self.max_length
        for field in Model._meta.fields:
            if field.name == self.instance_field:
                max_length = field.max_length
        name, ext = os.path.splitext(os.path.basename(filename))
        if callable(self.instance_field):
            value = self.instance_field(instance)
        else:
            value = getattr(instance, self.instance_field)

        filename = slugify_filename("%s%s" % (value[:max_length], ext))
        return os.path.join(self.base, datetime.now().strftime(self.strftime), filename)


def copy_file(file_):
    from django.core.files.base import ContentFile

    p = default_storage.save(file_.path, file_)
    return p
    path = file_.path
    while default_storage.exists(path):
        path, ext = os.path.splitext(path)
        path = "%s_%s" % (path, ext)
    p = default_storage.save(path, file_)
    print path, p
    return p


def duplicate(obj, value=None, field=None, duplicate_order=None):
    """
    Duplicate all related objects of obj setting
    field to value. If one of the duplicate
    objects has an FK to another duplicate object
    update that as well. Return the duplicate copy
    of obj.
    duplicate_order is a list of models which specify how
    the duplicate objects are saved. For complex objects
    this can matter. Check to save if objects are being
    saved correctly and if not just pass in related objects
    in the order that they should be saved.
    """
    from django.db.models.deletion import Collector
    from django.db.models.fields.related import ForeignKey
    from django.db.models import FileField

    collector = Collector({})
    collector.collect([obj])
    collector.sort()
    related_models = collector.data.keys()
    data_snapshot =  {}
    for key in collector.data.keys():
        data_snapshot.update({ key: dict(zip([item.pk for item in collector.data[key]], [item for item in collector.data[key]])) })
    root_obj = None

    # Sometimes it's good enough just to save in reverse deletion order.
    if duplicate_order is None:
        duplicate_order = reversed(related_models)

    for model in duplicate_order:
        # Find all FKs on model that point to a related_model.
        fks = []
        files = []
        for f in model._meta.fields:
            if isinstance(f, FileField):
                files.append(f)
            if isinstance(f, ForeignKey) and f.rel.to in related_models:
                fks.append(f)
        # Replace each `sub_obj` with a duplicate.
        if model not in collector.data:
            continue
        sub_objects = collector.data[model]
        for obj in sorted(sub_objects, key=attrgetter('id')):
            for ff in files:
                v = getattr(obj, ff.name, None)
                if v:
                    setattr(obj, ff.name, default_storage.save(v.name, v))
            for fk in fks:
                fk_value = getattr(obj, "%s_id" % fk.name)
                # If this FK has been duplicated then point to the duplicate.
                fk_rel_to = data_snapshot[fk.rel.to]
                if fk_value in fk_rel_to:
                    dupe_obj = fk_rel_to[fk_value]
                    setattr(obj, fk.name, dupe_obj)
            # Duplicate the object and save it.
            obj.id = None
            if field is not None:
                setattr(obj, field, value)
            obj.save()
            if root_obj is None:
                root_obj = obj
    return root_obj

