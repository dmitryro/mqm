# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Marker'
        db.create_table(u'local_map_marker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('icon', self.gf('mediastore.fields.related.MediaField')(related_name='marker_image', to=orm['mediastore.Media'])),
        ))
        db.send_create_signal(u'local_map', ['Marker'])

        # Adding model 'Map'
        db.create_table(u'local_map_map', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=120, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('privacy', self.gf('website.privacy.fields.PrivacyField')(default='national', max_length=12)),
            ('marker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['local_map.Marker'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'local_map', ['Map'])

        # Adding model 'Resource'
        db.create_table(u'local_map_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('privacy', self.gf('website.privacy.fields.PrivacyField')(default='national', max_length=12)),
        ))
        db.send_create_signal(u'local_map', ['Resource'])


    def backwards(self, orm):
        # Deleting model 'Marker'
        db.delete_table(u'local_map_marker')

        # Deleting model 'Map'
        db.delete_table(u'local_map_map')

        # Deleting model 'Resource'
        db.delete_table(u'local_map_resource')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'local_map.map': {
            'Meta': {'object_name': 'Map'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '120', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['local_map.Marker']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'privacy': ('website.privacy.fields.PrivacyField', [], {'default': "'national'", 'max_length': '12'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'local_map.marker': {
            'Meta': {'object_name': 'Marker'},
            'icon': ('mediastore.fields.related.MediaField', [], {'related_name': "'marker_image'", 'to': "orm['mediastore.Media']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'local_map.resource': {
            'Meta': {'object_name': 'Resource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privacy': ('website.privacy.fields.PrivacyField', [], {'default': "'national'", 'max_length': '12'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mediastore.media': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Media'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['local_map']
