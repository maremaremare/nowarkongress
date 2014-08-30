# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.topic'
        db.add_column(u'person_blogpost', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='blogposts', to=orm['news.ActualTopic']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.topic'
        db.delete_column(u'person_blogpost', 'topic_id')


    models = {
        u'news.actualtopic': {
            'Meta': {'object_name': 'ActualTopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_actual_now': ('django.db.models.fields.BooleanField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'person.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogposts'", 'to': u"orm['person.Person']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogposts'", 'to': u"orm['news.ActualTopic']"})
        },
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'person.product': {
            'Meta': {'object_name': 'Product'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['person.Person']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['person']