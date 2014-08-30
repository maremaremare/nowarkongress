# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MenuItem.object_id'
        db.alter_column(u'menu_menuitem', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'MenuItem.content_type'
        db.alter_column(u'menu_menuitem', 'content_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'MenuItem.object_id'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.object_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MenuItem.object_id'
        db.alter_column(u'menu_menuitem', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')())

        # User chose to not deal with backwards NULL issues for 'MenuItem.content_type'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.content_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MenuItem.content_type'
        db.alter_column(u'menu_menuitem', 'content_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType']))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['menu.MenuItem']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['menu']