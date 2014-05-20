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
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('income_restricted', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('income_unrestricted', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('charity_no', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('charity_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('reserves', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('deficit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('statement', self.gf('django.db.models.fields.TextField')()),
            ('group_avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('chairman', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('chairman_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ceo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ceo_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ceo_telephone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('chair_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('staff_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('trustees_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('volunteers_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('trustees_active', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('trustees_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('volunteers_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('staff_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=50)),
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
            'address': ('django.db.models.fields.TextField', [], {}),
            'ceo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ceo_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'ceo_telephone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'chair_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'chairman': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'chairman_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'charity_no': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'charity_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'deficit': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_restricted': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'income_unrestricted': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reserves': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('name',)", 'overwrite': 'False'}),
            'staff_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'staff_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'statement': ('django.db.models.fields.TextField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'trustees_active': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'trustees_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'trustees_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'volunteers_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'volunteers_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['local_minds']
