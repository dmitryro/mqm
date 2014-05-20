# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ethnicity'
        db.create_table(u'local_minds_ethnicity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'local_minds', ['Ethnicity'])

        # Deleting field 'LocalMind.trustees_ethnicity'
        db.delete_column(u'local_minds_localmind', 'trustees_ethnicity')

        # Deleting field 'LocalMind.staff_ethnicity'
        db.delete_column(u'local_minds_localmind', 'staff_ethnicity')

        # Deleting field 'LocalMind.volunteers_ethnicity'
        db.delete_column(u'local_minds_localmind', 'volunteers_ethnicity')

        # Adding M2M table for field trustees_ethnicities on 'LocalMind'
        m2m_table_name = db.shorten_name(u'local_minds_localmind_trustees_ethnicities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('localmind', models.ForeignKey(orm[u'local_minds.localmind'], null=False)),
            ('ethnicity', models.ForeignKey(orm[u'local_minds.ethnicity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['localmind_id', 'ethnicity_id'])

        # Adding M2M table for field volunteers_ethnicities on 'LocalMind'
        m2m_table_name = db.shorten_name(u'local_minds_localmind_volunteers_ethnicities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('localmind', models.ForeignKey(orm[u'local_minds.localmind'], null=False)),
            ('ethnicity', models.ForeignKey(orm[u'local_minds.ethnicity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['localmind_id', 'ethnicity_id'])

        # Adding M2M table for field staff_ethnicities on 'LocalMind'
        m2m_table_name = db.shorten_name(u'local_minds_localmind_staff_ethnicities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('localmind', models.ForeignKey(orm[u'local_minds.localmind'], null=False)),
            ('ethnicity', models.ForeignKey(orm[u'local_minds.ethnicity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['localmind_id', 'ethnicity_id'])


        # Renaming column for 'LocalMind.chair_ethnicity' to match new field type.
        db.rename_column(u'local_minds_localmind', 'chair_ethnicity', 'chair_ethnicity_id')
        # Changing field 'LocalMind.chair_ethnicity'
        db.alter_column(u'local_minds_localmind', 'chair_ethnicity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['local_minds.Ethnicity']))
        # Adding index on 'LocalMind', fields ['chair_ethnicity']
        db.create_index(u'local_minds_localmind', ['chair_ethnicity_id'])


    def backwards(self, orm):
        # Removing index on 'LocalMind', fields ['chair_ethnicity']
        db.delete_index(u'local_minds_localmind', ['chair_ethnicity_id'])

        # Deleting model 'Ethnicity'
        db.delete_table(u'local_minds_ethnicity')

        # Adding field 'LocalMind.trustees_ethnicity'
        db.add_column(u'local_minds_localmind', 'trustees_ethnicity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.staff_ethnicity'
        db.add_column(u'local_minds_localmind', 'staff_ethnicity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'LocalMind.volunteers_ethnicity'
        db.add_column(u'local_minds_localmind', 'volunteers_ethnicity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Removing M2M table for field trustees_ethnicities on 'LocalMind'
        db.delete_table(db.shorten_name(u'local_minds_localmind_trustees_ethnicities'))

        # Removing M2M table for field volunteers_ethnicities on 'LocalMind'
        db.delete_table(db.shorten_name(u'local_minds_localmind_volunteers_ethnicities'))

        # Removing M2M table for field staff_ethnicities on 'LocalMind'
        db.delete_table(db.shorten_name(u'local_minds_localmind_staff_ethnicities'))


        # Renaming column for 'LocalMind.chair_ethnicity' to match new field type.
        db.rename_column(u'local_minds_localmind', 'chair_ethnicity_id', 'chair_ethnicity')
        # Changing field 'LocalMind.chair_ethnicity'
        db.alter_column(u'local_minds_localmind', 'chair_ethnicity', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

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
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
        }
    }

    complete_apps = ['local_minds']