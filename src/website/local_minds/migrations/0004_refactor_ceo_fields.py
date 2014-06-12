# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'local_minds_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ethnicity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['local_minds.Ethnicity'], null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'local_minds', ['Person'])

        # Deleting field 'LocalMind.ceo'
        db.delete_column(u'local_minds_localmind', 'ceo')

        # Deleting field 'LocalMind.ceo_email'
        db.delete_column(u'local_minds_localmind', 'ceo_email')

        # Deleting field 'LocalMind.ceo_telephone'
        db.delete_column(u'local_minds_localmind', 'ceo_telephone')

        # Deleting field 'LocalMind.chairman_email'
        db.delete_column(u'local_minds_localmind', 'chairman_email')

        # Deleting field 'LocalMind.chairman'
        db.delete_column(u'local_minds_localmind', 'chairman')

        # Deleting field 'LocalMind.chair_ethnicity'
        db.delete_column(u'local_minds_localmind', 'chair_ethnicity_id')

        # Adding field 'LocalMind.ceo_one'
        db.add_column(u'local_minds_localmind', 'ceo_one',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ceo_one_of', null=True, to=orm['local_minds.Person']),
                      keep_default=False)

        # Adding field 'LocalMind.ceo_two'
        db.add_column(u'local_minds_localmind', 'ceo_two',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ceo_two_of', null=True, to=orm['local_minds.Person']),
                      keep_default=False)

        # Adding field 'LocalMind.chair'
        db.add_column(u'local_minds_localmind', 'chair',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='chair_one_of', null=True, to=orm['local_minds.Person']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'local_minds_person')

        # Adding field 'LocalMind.ceo'
        db.add_column(u'local_minds_localmind', 'ceo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.ceo_email'
        db.add_column(u'local_minds_localmind', 'ceo_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.ceo_telephone'
        db.add_column(u'local_minds_localmind', 'ceo_telephone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.chairman_email'
        db.add_column(u'local_minds_localmind', 'chairman_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.chairman'
        db.add_column(u'local_minds_localmind', 'chairman',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.chair_ethnicity'
        db.add_column(u'local_minds_localmind', 'chair_ethnicity',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='chair_ethnicity+', null=True, to=orm['local_minds.Ethnicity'], blank=True),
                      keep_default=False)

        # Deleting field 'LocalMind.ceo_one'
        db.delete_column(u'local_minds_localmind', 'ceo_one_id')

        # Deleting field 'LocalMind.ceo_two'
        db.delete_column(u'local_minds_localmind', 'ceo_two_id')

        # Deleting field 'LocalMind.chair'
        db.delete_column(u'local_minds_localmind', 'chair_id')


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
            'ceo_one': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ceo_one_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
            'ceo_two': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ceo_two_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'chair_one_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
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
        u'local_minds.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['local_minds.Ethnicity']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['local_minds']