# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MenuItem'
        db.create_table(u'menu_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'menu', ['MenuItem'])


    def backwards(self, orm):
        # Deleting model 'MenuItem'
        db.delete_table(u'menu_menuitem')


    models = {
        u'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['menu']