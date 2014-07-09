# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'faq_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('list_image', self.gf('mediastore.fields.related.MediaField')(blank=True, related_name='faq_category_image', null=True, to=orm['mediastore.Media'])),
            ('sort_value', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'faq', ['Category'])

        # Adding M2M table for field categories on 'Question'
        m2m_table_name = db.shorten_name(u'faq_question_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'faq.question'], null=False)),
            ('category', models.ForeignKey(orm[u'faq.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'faq_category')

        # Removing M2M table for field categories on 'Question'
        db.delete_table(db.shorten_name(u'faq_question_categories'))


    models = {
        u'accounts.skill': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('name',)", 'overwrite': 'False'})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'biography': ('django.db.models.fields.TextField', [], {'max_length': '350', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'email': ('website.utils.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'users'", 'null': 'True', 'to': u"orm['local_minds.LocalMind']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'privileges': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.Skill']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('first_name', 'last_name')", 'overwrite': 'False'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'faq.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['faq.Question']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['accounts.User']"})
        },
        u'faq.category': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_image': ('mediastore.fields.related.MediaField', [], {'blank': 'True', 'related_name': "'faq_category_image'", 'null': 'True', 'to': "orm['mediastore.Media']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'faq.question': {
            'Meta': {'object_name': 'Question'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'questions'", 'blank': 'True', 'to': u"orm['faq.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['local_minds.LocalMind']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'notifications': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'privacy': ('website.privacy.fields.PrivacyField', [], {'default': "'national'", 'max_length': '12'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['accounts.User']"})
        },
        u'local_minds.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'local_minds.localmind': {
            'Meta': {'object_name': 'LocalMind'},
            '_latitude_postcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            '_longitude_postcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'area_of_benefit': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
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
            'trustees_active': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['faq']