# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'faq_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local_mind', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['local_minds.LocalMind'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='question', null=True, to=orm['accounts.User'])),
            ('notifications', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('privacy', self.gf('website.privacy.fields.PrivacyField')(default='national', max_length=12)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'faq', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'faq_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faq.Question'])),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='answer', null=True, to=orm['accounts.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'faq', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'faq_question')

        # Deleting model 'Answer'
        db.delete_table(u'faq_answer')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('website.utils.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'skills': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'answer'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faq.Question']"})
        },
        u'faq.question': {
            'Meta': {'object_name': 'Question'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'question'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['local_minds.LocalMind']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'notifications': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'privacy': ('website.privacy.fields.PrivacyField', [], {'default': "'national'", 'max_length': '12'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '140'})
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
        }
    }

    complete_apps = ['faq']