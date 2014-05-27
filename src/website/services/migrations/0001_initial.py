# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'services_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local_mind', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['local_minds.LocalMind'])),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from=('name',), overwrite=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('users_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'services', ['Service'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'services_service')


    models = {
        u'local_minds.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'local_minds.localmind': {
            'Meta': {'object_name': 'LocalMind'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ceo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ceo_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'ceo_telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'chair_ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'chair_ethnicity+'", 'null': 'True', 'to': u"orm['local_minds.Ethnicity']"}),
            'chairman': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'chairman_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'charity_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'charity_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'deficit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'group_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_restricted': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'income_unrestricted': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reserves': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('name',)", 'overwrite': 'False'}),
            'staff_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'staff_ethnicities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff+'", 'blank': 'True', 'to': u"orm['local_minds.Ethnicity']"}),
            'statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trustees_active': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trustees_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trustees_ethnicities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'trustees+'", 'blank': 'True', 'to': u"orm['local_minds.Ethnicity']"}),
            'volunteers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteers_ethnicities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'volunteers+'", 'blank': 'True', 'to': u"orm['local_minds.Ethnicity']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'services.service': {
            'Meta': {'object_name': 'Service'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['local_minds.LocalMind']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('name',)", 'overwrite': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'users_count': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['services']
