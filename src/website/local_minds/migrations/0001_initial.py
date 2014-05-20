# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalMind'
        db.create_table(u'local_minds_localmind', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from=('name',), overwrite=False)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('income_restricted', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('income_unrestricted', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('charity_no', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('charity_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('reserves', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('deficit', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('statement', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('group_avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('chairman', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('chairman_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('ceo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ceo_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('ceo_telephone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('chair_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('staff_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('trustees_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('volunteers_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('trustees_active', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('trustees_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('volunteers_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('staff_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'local_minds', ['LocalMind'])


    def backwards(self, orm):
        # Deleting model 'LocalMind'
        db.delete_table(u'local_minds_localmind')


    models = {
        u'local_minds.localmind': {
            'Meta': {'object_name': 'LocalMind'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ceo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ceo_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'ceo_telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'chair_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
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
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reserves': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('name',)", 'overwrite': 'False'}),
            'staff_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'staff_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trustees_active': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trustees_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trustees_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'volunteers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteers_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['local_minds']