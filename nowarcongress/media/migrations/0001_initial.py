# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'media_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('photo_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo', to=orm['contenttypes.ContentType'])),
            ('photo_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'media', ['Photo'])

        # Adding model 'Video'
        db.create_table(u'media_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
            ('video_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='video', to=orm['contenttypes.ContentType'])),
            ('video_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'media', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'media_photo')

        # Deleting model 'Video'
        db.delete_table(u'media_video')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'media.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo'", 'to': u"orm['contenttypes.ContentType']"}),
            'photo_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'media.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'}),
            'video_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'video'", 'to': u"orm['contenttypes.ContentType']"}),
            'video_object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['media']