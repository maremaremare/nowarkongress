# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePageSection'
        db.create_table(u'main_homepagesection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.ActualTopic'], null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['HomePageSection'])

        # Adding model 'SliderItem'
        db.create_table(u'main_slideritem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='relatedcontents', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('parent_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_test_link', to=orm['contenttypes.ContentType'])),
            ('parent_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slideritem', to=orm['media.Photo'])),
        ))
        db.send_create_signal(u'main', ['SliderItem'])

        # Adding model 'ActualSlider'
        db.create_table(u'main_actualslider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ActualSlider'])

        # Adding model 'Partner'
        db.create_table(u'main_partner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'main', ['Partner'])


    def backwards(self, orm):
        # Deleting model 'HomePageSection'
        db.delete_table(u'main_homepagesection')

        # Deleting model 'SliderItem'
        db.delete_table(u'main_slideritem')

        # Deleting model 'ActualSlider'
        db.delete_table(u'main_actualslider')

        # Deleting model 'Partner'
        db.delete_table(u'main_partner')


    models = {
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
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.ActualTopic']", 'null': 'True', 'blank': 'True'})
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
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relatedcontents'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_test_link'", 'to': u"orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
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
        u'news.actualtopic': {
            'Meta': {'object_name': 'ActualTopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_actual_now': ('django.db.models.fields.BooleanField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']