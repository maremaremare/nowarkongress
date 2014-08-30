# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Petition'
        db.create_table(u'events_petition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.ContentItem'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Petition'])

        # Adding M2M table for field participators on 'Petition'
        m2m_table_name = db.shorten_name(u'events_petition_participators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('petition', models.ForeignKey(orm[u'events.petition'], null=False)),
            ('person', models.ForeignKey(orm[u'person.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['petition_id', 'person_id'])

        # Adding model 'EventItem'
        db.create_table(u'events_eventitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('announcement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='announcements', to=orm['content.ContentItem'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', to=orm['content.ContentItem'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'events', ['EventItem'])

        # Adding M2M table for field participants on 'EventItem'
        m2m_table_name = db.shorten_name(u'events_eventitem_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventitem', models.ForeignKey(orm[u'events.eventitem'], null=False)),
            ('person', models.ForeignKey(orm[u'person.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['eventitem_id', 'person_id'])

        # Adding M2M table for field lectures on 'EventItem'
        m2m_table_name = db.shorten_name(u'events_eventitem_lectures')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventitem', models.ForeignKey(orm[u'events.eventitem'], null=False)),
            ('contentitem', models.ForeignKey(orm[u'content.contentitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['eventitem_id', 'contentitem_id'])


    def backwards(self, orm):
        # Deleting model 'Petition'
        db.delete_table(u'events_petition')

        # Removing M2M table for field participators on 'Petition'
        db.delete_table(db.shorten_name(u'events_petition_participators'))

        # Deleting model 'EventItem'
        db.delete_table(u'events_eventitem')

        # Removing M2M table for field participants on 'EventItem'
        db.delete_table(db.shorten_name(u'events_eventitem_participants'))

        # Removing M2M table for field lectures on 'EventItem'
        db.delete_table(db.shorten_name(u'events_eventitem_lectures'))


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
        u'events.eventitem': {
            'Meta': {'object_name': 'EventItem'},
            'announcement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcements'", 'to': u"orm['content.ContentItem']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lectures': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lectures'", 'symmetrical': 'False', 'to': u"orm['content.ContentItem']"}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['person.Person']", 'symmetrical': 'False'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': u"orm['content.ContentItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'events.petition': {
            'Meta': {'object_name': 'Petition'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['person.Person']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.ContentItem']"}),
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
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['events']