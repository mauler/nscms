# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SimpleNewsletter'
        db.create_table('simplenewsletter_simplenewsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
        ))
        db.send_create_signal('simplenewsletter', ['SimpleNewsletter'])


    def backwards(self, orm):
        # Deleting model 'SimpleNewsletter'
        db.delete_table('simplenewsletter_simplenewsletter')


    models = {
        'simplenewsletter.simplenewsletter': {
            'Meta': {'ordering': "['-created']", 'object_name': 'SimpleNewsletter'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['simplenewsletter']