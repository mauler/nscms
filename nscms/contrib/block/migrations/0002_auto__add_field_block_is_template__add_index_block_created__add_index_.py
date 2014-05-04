# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Block.is_template'
        db.add_column(u'block_block', 'is_template',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding index on 'Block', fields ['created']
        db.create_index(u'block_block', ['created'])

        # Adding index on 'Block', fields ['modified']
        db.create_index(u'block_block', ['modified'])


        # Changing field 'Block.content'
        db.alter_column(u'block_block', 'content', self.gf('django.db.models.fields.TextField')())
        # Adding index on 'Block', fields ['publish_date']
        db.create_index(u'block_block', ['publish_date'])

        # Adding index on 'Block', fields ['expire_date']
        db.create_index(u'block_block', ['expire_date'])

        # Adding index on 'Block', fields ['published']
        db.create_index(u'block_block', ['published'])


    def backwards(self, orm):
        # Removing index on 'Block', fields ['published']
        db.delete_index(u'block_block', ['published'])

        # Removing index on 'Block', fields ['expire_date']
        db.delete_index(u'block_block', ['expire_date'])

        # Removing index on 'Block', fields ['publish_date']
        db.delete_index(u'block_block', ['publish_date'])

        # Removing index on 'Block', fields ['modified']
        db.delete_index(u'block_block', ['modified'])

        # Removing index on 'Block', fields ['created']
        db.delete_index(u'block_block', ['created'])

        # Deleting field 'Block.is_template'
        db.delete_column(u'block_block', 'is_template')


        # Changing field 'Block.content'
        db.alter_column(u'block_block', 'content', self.gf('ckeditor.fields.RichTextField')())

    models = {
        u'block.block': {
            'Meta': {'object_name': 'Block'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '255', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['block']