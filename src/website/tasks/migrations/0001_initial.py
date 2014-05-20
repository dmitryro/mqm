# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local_mind', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['local_minds.LocalMind'])),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from='text', overwrite=False)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('done_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sort_value', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('is_priority', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tasks', null=True, to=orm['accounts.User'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_tasks', to=orm['accounts.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'tasks', ['Task'])

        # Adding model 'Comment'
        db.create_table(u'tasks_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['tasks.Task'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='task_comments', to=orm['accounts.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'tasks', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'tasks_task')

        # Deleting model 'Comment'
        db.delete_table(u'tasks_comment')


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
        },
        u'tasks.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_comments'", 'to': u"orm['accounts.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['tasks.Task']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'tasks.task': {
            'Meta': {'ordering': "('local_mind', 'sort_value')", 'object_name': 'Task'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tasks'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tasks'", 'to': u"orm['accounts.User']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'done_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_priority': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'local_mind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': u"orm['local_minds.LocalMind']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'text'", 'overwrite': 'False'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tasks']