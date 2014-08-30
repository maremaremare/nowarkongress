# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MenuItem.order'
        db.delete_column(u'menu_menuitem', 'order')

        # Deleting field 'MenuItem.topic'
        db.delete_column(u'menu_menuitem', 'topic_id')

        # Adding field 'MenuItem.parent'
        db.add_column(u'menu_menuitem', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['menu.MenuItem']),
                      keep_default=False)

        # Adding field 'MenuItem.content_type'
        db.add_column(u'menu_menuitem', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Adding field 'MenuItem.object_id'
        db.add_column(u'menu_menuitem', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'MenuItem.lft'
        db.add_column(u'menu_menuitem', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'MenuItem.rght'
        db.add_column(u'menu_menuitem', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'MenuItem.tree_id'
        db.add_column(u'menu_menuitem', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'MenuItem.level'
        db.add_column(u'menu_menuitem', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'MenuItem.path'
        db.alter_column(u'menu_menuitem', 'path', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'MenuItem.subtitle'
        db.alter_column(u'menu_menuitem', 'subtitle', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'MenuItem.order'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.order' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'MenuItem.order'
        db.add_column(u'menu_menuitem', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True),
                      keep_default=False)

        # Adding field 'MenuItem.topic'
        db.add_column(u'menu_menuitem', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.ActualTopic'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MenuItem.parent'
        db.delete_column(u'menu_menuitem', 'parent_id')

        # Deleting field 'MenuItem.content_type'
        db.delete_column(u'menu_menuitem', 'content_type_id')

        # Deleting field 'MenuItem.object_id'
        db.delete_column(u'menu_menuitem', 'object_id')

        # Deleting field 'MenuItem.lft'
        db.delete_column(u'menu_menuitem', u'lft')

        # Deleting field 'MenuItem.rght'
        db.delete_column(u'menu_menuitem', u'rght')

        # Deleting field 'MenuItem.tree_id'
        db.delete_column(u'menu_menuitem', u'tree_id')

        # Deleting field 'MenuItem.level'
        db.delete_column(u'menu_menuitem', u'level')


        # User chose to not deal with backwards NULL issues for 'MenuItem.path'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.path' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MenuItem.path'
        db.alter_column(u'menu_menuitem', 'path', self.gf('django.db.models.fields.CharField')(max_length=200))

        # User chose to not deal with backwards NULL issues for 'MenuItem.subtitle'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.subtitle' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MenuItem.subtitle'
        db.alter_column(u'menu_menuitem', 'subtitle', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['menu.MenuItem']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['menu']