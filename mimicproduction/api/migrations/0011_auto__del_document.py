# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'api_document')


    def backwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'api_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'api', ['Document'])


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