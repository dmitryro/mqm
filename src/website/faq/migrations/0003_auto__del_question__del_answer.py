# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'faq_question')

        # Deleting model 'Answer'
        db.delete_table(u'faq_answer')


    def backwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'faq_question', (
            ('notifications', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['accounts.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('privacy', self.gf('website.privacy.fields.PrivacyField')(default='national', max_length=12)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=140)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local_mind', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['local_minds.LocalMind'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'faq', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'faq_answer', (
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer', to=orm['accounts.User'])),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['faq.Question'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'faq', ['Answer'])


    models = {
        
    }

    complete_apps = ['faq']