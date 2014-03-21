# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'api.comments': {
            'Meta': {'object_name': 'Comments'},
            'commentid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'commentlink': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'postidcommentedon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Post']"}),
            'useridcommenter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
        },
        u'api.post': {
            'Createdthispost': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Posts'", 'null': 'True', 'to': u"orm['api.User']"}),
            'Meta': {'object_name': 'Post'},
            'Userwhodidit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']", 'null': 'True'}),
            'commentcounter': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
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
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'userid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['api']
    symmetrical = True
