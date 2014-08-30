# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Photo.photo_content_type'
        db.delete_column(u'media_photo', 'photo_content_type_id')

        # Deleting field 'Photo.photo_object_id'
        db.delete_column(u'media_photo', 'photo_object_id')

        # Adding field 'Photo.content'
        db.add_column(u'media_photo', 'content',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['content.ContentItem']),
                      keep_default=False)

        # Deleting field 'Video.video_object_id'
        db.delete_column(u'media_video', 'video_object_id')

        # Deleting field 'Video.video_content_type'
        db.delete_column(u'media_video', 'video_content_type_id')

        # Adding field 'Video.content'
        db.add_column(u'media_video', 'content',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['content.ContentItem']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Photo.photo_content_type'
        raise RuntimeError("Cannot reverse this migration. 'Photo.photo_content_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.photo_content_type'
        db.add_column(u'media_photo', 'photo_content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo', to=orm['contenttypes.ContentType']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.photo_object_id'
        raise RuntimeError("Cannot reverse this migration. 'Photo.photo_object_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.photo_object_id'
        db.add_column(u'media_photo', 'photo_object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)

        # Deleting field 'Photo.content'
        db.delete_column(u'media_photo', 'content_id')


        # User chose to not deal with backwards NULL issues for 'Video.video_object_id'
        raise RuntimeError("Cannot reverse this migration. 'Video.video_object_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Video.video_object_id'
        db.add_column(u'media_video', 'video_object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Video.video_content_type'
        raise RuntimeError("Cannot reverse this migration. 'Video.video_content_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Video.video_content_type'
        db.add_column(u'media_video', 'video_content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='video', to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Deleting field 'Video.content'
        db.delete_column(u'media_video', 'content_id')


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
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['content.Topic']"})
        },
        u'content.sidebaritem': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SidebarItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'context_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'for_detail_only': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'content.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'media.photo': {
            'Meta': {'object_name': 'Photo'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.ContentItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'media.video': {
            'Meta': {'object_name': 'Video'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.ContentItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
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

    complete_apps = ['media']