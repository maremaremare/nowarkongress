# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OuterParticipant'
        db.create_table(u'content_outerparticipant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'content', ['OuterParticipant'])

        # Adding model 'Petition'
        db.create_table(u'content_petition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'content', ['Petition'])

        # Adding M2M table for field participants on 'Petition'
        m2m_table_name = db.shorten_name(u'content_petition_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('petition', models.ForeignKey(orm[u'content.petition'], null=False)),
            ('person', models.ForeignKey(orm[u'person.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['petition_id', 'person_id'])

        # Adding M2M table for field outerparticipants on 'Petition'
        m2m_table_name = db.shorten_name(u'content_petition_outerparticipants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('petition', models.ForeignKey(orm[u'content.petition'], null=False)),
            ('outerparticipant', models.ForeignKey(orm[u'content.outerparticipant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['petition_id', 'outerparticipant_id'])

        # Adding field 'ContentItem.petition'
        db.add_column(u'content_contentitem', 'petition',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='petition', null=True, to=orm['content.Petition']),
                      keep_default=False)

        # Adding field 'ContentItem.dateevent'
        db.add_column(u'content_contentitem', 'dateevent',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'OuterParticipant'
        db.delete_table(u'content_outerparticipant')

        # Deleting model 'Petition'
        db.delete_table(u'content_petition')

        # Removing M2M table for field participants on 'Petition'
        db.delete_table(db.shorten_name(u'content_petition_participants'))

        # Removing M2M table for field outerparticipants on 'Petition'
        db.delete_table(db.shorten_name(u'content_petition_outerparticipants'))

        # Deleting field 'ContentItem.petition'
        db.delete_column(u'content_contentitem', 'petition_id')

        # Deleting field 'ContentItem.dateevent'
        db.delete_column(u'content_contentitem', 'dateevent')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usergenerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'content.contentitem': {
            'Meta': {'ordering': "['-date']", 'object_name': 'ContentItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['person.Person']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['content.ContentCategory']"}),
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'dateevent': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'petition': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'petition'", 'null': 'True', 'to': u"orm['content.Petition']"}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['content.Topic']"})
        },
        u'content.outerparticipant': {
            'Meta': {'object_name': 'OuterParticipant'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'content.petition': {
            'Meta': {'object_name': 'Petition'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outerparticipants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'petition'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['content.OuterParticipant']"}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'petition'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['person.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'content.sidebaritem': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SidebarItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'context_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'for_detail_only': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
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
        u'person.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['content']