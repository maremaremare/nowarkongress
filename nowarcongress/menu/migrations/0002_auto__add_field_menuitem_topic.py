# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuItem.topic'
        db.add_column(u'menu_menuitem', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.ActualTopic'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuItem.topic'
        db.delete_column(u'menu_menuitem', 'topic_id')


    models = {
        u'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.ActualTopic']", 'null': 'True', 'blank': 'True'})
        },
        u'news.actualtopic': {
            'Meta': {'object_name': 'ActualTopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_actual_now': ('django.db.models.fields.BooleanField', [], {}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['news.ActualTopic']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['menu']