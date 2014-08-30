# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SliderItem.parent_object_id'
        db.delete_column(u'main_slideritem', 'parent_object_id')

        # Deleting field 'SliderItem.object_id'
        db.delete_column(u'main_slideritem', 'object_id')

        # Deleting field 'SliderItem.content_type'
        db.delete_column(u'main_slideritem', 'content_type_id')

        # Deleting field 'SliderItem.parent_content_type'
        db.delete_column(u'main_slideritem', 'parent_content_type_id')

        # Adding field 'SliderItem.order'
        db.add_column(u'main_slideritem', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'SliderItem.item'
        db.add_column(u'main_slideritem', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['content.ContentItem']),
                      keep_default=False)

        # Deleting field 'HomePageSection.title'
        db.delete_column(u'main_homepagesection', 'title')

        # Deleting field 'HomePageSection.topic'
        db.delete_column(u'main_homepagesection', 'topic_id')

        # Adding field 'HomePageSection.object_id'
        db.add_column(u'main_homepagesection', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SliderItem.parent_object_id'
        raise RuntimeError("Cannot reverse this migration. 'SliderItem.parent_object_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SliderItem.parent_object_id'
        db.add_column(u'main_slideritem', 'parent_object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SliderItem.object_id'
        raise RuntimeError("Cannot reverse this migration. 'SliderItem.object_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SliderItem.object_id'
        db.add_column(u'main_slideritem', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SliderItem.content_type'
        raise RuntimeError("Cannot reverse this migration. 'SliderItem.content_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SliderItem.content_type'
        db.add_column(u'main_slideritem', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='relatedcontents', to=orm['contenttypes.ContentType']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SliderItem.parent_content_type'
        raise RuntimeError("Cannot reverse this migration. 'SliderItem.parent_content_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SliderItem.parent_content_type'
        db.add_column(u'main_slideritem', 'parent_content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_test_link', to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Deleting field 'SliderItem.order'
        db.delete_column(u'main_slideritem', 'order')

        # Deleting field 'SliderItem.item'
        db.delete_column(u'main_slideritem', 'item_id')


        # User chose to not deal with backwards NULL issues for 'HomePageSection.title'
        raise RuntimeError("Cannot reverse this migration. 'HomePageSection.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'HomePageSection.title'
        db.add_column(u'main_homepagesection', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Adding field 'HomePageSection.topic'
        db.add_column(u'main_homepagesection', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.ActualTopic'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'HomePageSection.object_id'
        db.delete_column(u'main_homepagesection', 'object_id')


    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'content.contentcategory': {
            'Meta': {'object_name': 'ContentCategory'},
            'detail_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'list_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sidebar': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['content.SidebarItem']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'content.contentitem': {
            'Meta': {'object_name': 'ContentItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['person.Person']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['content.ContentCategory']"}),
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['content.Topic']"})
        },
        u'content.sidebaritem': {
            'Meta': {'object_name': 'SidebarItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'context_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'for_detail_only': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'content.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['content.Topic']"}),
            'public': ('django.db.models.fields.BooleanField', [], {}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.actualslider': {
            'Meta': {'object_name': 'ActualSlider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.homepagesection': {
            'Meta': {'ordering': "('order',)", 'object_name': 'HomePageSection'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'main.partner': {
            'Meta': {'object_name': 'Partner'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.slideritem': {
            'Meta': {'object_name': 'SliderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.ContentItem']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slideritem'", 'to': u"orm['media.Photo']"})
        },
        u'media.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo'", 'to': u"orm['contenttypes.ContentType']"}),
            'photo_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['main']