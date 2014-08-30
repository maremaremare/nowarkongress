# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'person_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('initial', self.gf('django.db.models.fields.BooleanField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('subscribed', self.gf('django.db.models.fields.BooleanField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'person', ['Person'])

        # Adding model 'BlogPost'
        db.create_table(u'person_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blogposts', to=orm['person.Person'])),
        ))
        db.send_create_signal(u'person', ['BlogPost'])

        # Adding model 'Product'
        db.create_table(u'person_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
        ))
        db.send_create_signal(u'person', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'person_person')

        # Deleting model 'BlogPost'
        db.delete_table(u'person_blogpost')

        # Deleting model 'Product'
        db.delete_table(u'person_product')


    models = {
        u'person.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogposts'", 'to': u"orm['person.Person']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
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