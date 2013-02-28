#!/usr/bin/env python
#-*- coding:utf-8 -*-

from simplejson import loads

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib import admin
from django.core.mail import EmailMessage, send_mail
from django.db.models import signals
from django.db import models
from django.template.loader import render_to_string

from django_extensions.db.fields.json import JSONField, dumps


class JSONField2(JSONField):

    def get_db_prep_save(self, value, connection):
        """Convert our JSON object to a string before we save"""
        if not isinstance(value, (list, dict)):
            return super(JSONField, self).get_db_prep_save("", connection=connection)
        else:
            return super(JSONField, self).get_db_prep_save(dumps(value),
                                                           connection=connection)

class MailModel(models.Model):
    template_name = getattr(settings, "CEMESE_MAILING_TEMPLATE_NAME", "cemese/mail_template.txt")
    mail_subject = getattr(settings, "CEMESE_MAILING_MAIL_SUBJECT", "Cemese mail")
    from_mail = getattr(settings, "CEMESE_MAILING_FROM_MAIL", "contato@construtoracarrara.com.br")
    to_mail = getattr(settings, "CEMESE_MAILING_TO_MAIL", ["proberto.macedo@gmail.com"])
    fail_silently = getattr(settings, "CEMESE_MAILING_FAIL_SILENTLY", True)

    mail_sent = models.BooleanField(verbose_name=u"Email enviado",
                                    default=False,
                                    editable=True)

    class Admin(admin.ModelAdmin):
        readonly_fields = ("mail_sent", )

    class Meta:
        abstract = True

    def send_email(self):
        if not self.mail_sent:
            if hasattr(self, "mailing"):
                for subject, template_name, getto in self.mailing:
                    html_content = render_to_string(template_name, {'instance': self})

                    if callable(subject):
                        subject = subject(self)

                    if callable(getto):
                        to = getto(self)
                    else:
                        to = self.to_mail

                    msg = EmailMessage(subject, html_content, self.from_mail, to)
                    if template_name.endswith(".html"):
                        msg.content_subtype = "html"
                    msg.send()
            else:
                message = render_to_string(self.template_name, {'instance': self})
                send_mail(self.mail_subject,
                          message,
                          self.from_mail,
                          self.to_mail,
                          fail_silently=self.fail_silently)
            self.mail_sent = True
            self.save()
            return True
        else:
            return False

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            instance.send_email()

class MailmeModel(object):
    mailme = True

class Mailme(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    template_name = models.CharField(max_length=255, default=getattr(settings, "CEMESE_MAILING_TEMPLATE_NAME", "cemese/mail_template.txt"))
    mail_content = models.TextField(blank=True)
    mail_subject = models.CharField(max_length=255, default=getattr(settings, "CEMESE_MAILING_MAIL_SUBJECT", "[CEMESE] mailing.Mailme"))
    from_mail = models.CharField(max_length=255, default=getattr(settings, "CEMESE_MAILING_FROM_MAIL", "proberto.macedo@gmail.com"))
    to_mail = JSONField2(default=getattr(settings, "CEMESE_MAILING_TO_MAIL", ["proberto.macedo@gmail.com"]))
    fail_silently = models.CharField(max_length=255, default=getattr(settings, "CEMESE_MAILING_FAIL_SILENTLY", True))
    sent = models.BooleanField(verbose_name=u"Email enviado", default=False)#, null=True)#, editable=True, null=True)

    class Admin(admin.ModelAdmin):
        readonly_fields = ("sent", "fail_silently", )

    def send_mail(self, context={}):
        context.update({'object': self.content_object, 'instance': self})
        html_content = render_to_string(self.template_name, context)
        msg = EmailMessage(self.mail_subject.strip(),
                           self.mail_content or html_content,
                           self.from_mail,
                           self.to_mail['to'])
        if self.template_name.endswith(".html"):
            msg.content_subtype = "html"
        self.sent = msg.send(fail_silently=self.fail_silently)
        self.save()

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created and not instance.sent:
            if not instance.sent:
                instance.send_mail()
#                html_content = render_to_string(instance.template_name,
#                                                {'instance': instance,
#                                                 'object': self.content_object})
#                msg = EmailMessage(instance.mail_subject,
#                                   html_content,
#                                   instance.from_mail,
#                                   instance.to_mail)
#                if instance.template_name.endswith(".html"):
#                    msg.content_subtype = "html"
#                instance.sent = msg.send(fail_silently=instance.fail_silently)
#                instance.save()

    @staticmethod
    def plugged_model_post_save(sender, instance, created, *args, **kwargs):
        if getattr(instance, 'mailme', False) and created:
            for i in instance.get_mailme():
                Mailme.objects.create(content_object=instance, **i)

signals.post_save.connect(Mailme.post_save, sender=Mailme)

signals.post_save.connect(Mailme.plugged_model_post_save)

