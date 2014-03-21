# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'api_user', (
            ('userid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=70)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('Username', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('followers', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('following', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('likes', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['User'])

        # Adding model 'Post'
        db.create_table(u'api_post', (
            ('postid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Userpostid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('postlink', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('likecounter', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('share', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('comment', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'api', ['Post'])

        # Adding model 'Comments'
        db.create_table(u'api_comments', (
            ('commentid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('useridcommenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('postidcommentedon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Post'])),
            ('commentlink', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'api', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'api_user')

        # Deleting model 'Post'
        db.delete_table(u'api_post')

        # Deleting model 'Comments'
        db.delete_table(u'api_comments')


    models = {
        u'api.comments': {
            'Meta': {'object_name': 'Comments'},
            'commentid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'commentlink': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'postidcommentedon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Post']"}),
            'useridcommenter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
        },
        u'api.post': {
            'Meta': {'object_name': 'Post'},
            'Userpostid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"}),
            'comment': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'likecounter': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'postid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postlink': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'share': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'api.user': {
            'Meta': {'object_name': 'User'},
            'Username': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'followers': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'following': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'likes': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'userid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['api']