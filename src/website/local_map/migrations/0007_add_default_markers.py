# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    icons = [
        'local_map/markers/potential/reach.png',
        'local_map/markers/potential/cruse.png',
        'local_map/markers/potential/samaritans.png',
        'local_map/markers/potential/rethink.png',
        'local_map/markers/potential/national-charity.png',
        'local_map/markers/potential/relate.png',
        'local_map/markers/potential/housing-association.png',
        'local_map/markers/potential/ymca.png',
        'local_map/markers/potential/mencap.png',
        'local_map/markers/potential/private-company.png',
        'local_map/markers/potential/local-authority.png',
        'local_map/markers/potential/child-povery-action-group.png',
        'local_map/markers/potential/turning-point.png',
        'local_map/markers/potential/macmillan.png',
        'local_map/markers/potential/age-uk.png',
        'local_map/markers/potential/family-action.png',
        'local_map/markers/potential/local-charity.png',
        'local_map/markers/potential/nhs-body.png',
        'local_map/markers/potential/cab.png',
        'local_map/markers/potential/national-trust.png',
        'local_map/markers/potential/alturnatives-to-violence-project.png',
        'local_map/markers/current/reach.png',
        'local_map/markers/current/cruse.png',
        'local_map/markers/current/samaritans.png',
        'local_map/markers/current/rethink.png',
        'local_map/markers/current/national-charity.png',
        'local_map/markers/current/relate.png',
        'local_map/markers/current/housing-association.png',
        'local_map/markers/current/ymca.png',
        'local_map/markers/current/mencap.png',
        'local_map/markers/current/private-company.png',
        'local_map/markers/current/local-authority.png',
        'local_map/markers/current/child-povery-action-group.png',
        'local_map/markers/current/turning-point.png',
        'local_map/markers/current/macmillan.png',
        'local_map/markers/current/age-uk.png',
        'local_map/markers/current/family-action.png',
        'local_map/markers/current/local-charity.png',
        'local_map/markers/current/nhs-body.png',
        'local_map/markers/current/cab.png',
        'local_map/markers/current/national-trust.png',
        'local_map/markers/current/alturnatives-to-violence-project.png',
        'local_map/markers/current.png',
        'local_map/markers/potential.png',
        'local_map/markers/funding.png',
        'local_map/markers/local-mind.png',
    ]

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        Marker = orm['local_map.Marker']

        for icon in self.icons:
            marker = Marker.objects.filter(icon=icon)
            if not marker.exists():
                name = icon[len('local_map/markers/'):]
                name = name[:-len('.png')]
                name = name.replace('/', ': ')
                name = name.replace('-', ' ')
                Marker.objects.create(
                    title=name,
                    icon=icon)

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'local_map.map': {
            'Meta': {'object_name': 'Map'},
            '_latitude_postcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            '_longitude_postcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '120', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners'", 'to': u"orm['local_minds.LocalMind']"}),
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
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'local_minds.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'local_minds.localmind': {
            'Meta': {'object_name': 'LocalMind'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'area_of_benefit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'average_volunteer_hours': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ceo_one': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ceo_one_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
            'ceo_two': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ceo_two_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'chair_one_of'", 'null': 'True', 'to': u"orm['local_minds.Person']"}),
            'charity_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'charity_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'deficit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'group_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'hours': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trustees_active': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trustees_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['local_map']
    symmetrical = True
