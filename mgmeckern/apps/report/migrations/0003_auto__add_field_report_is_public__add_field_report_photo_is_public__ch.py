# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Report.is_public'
        db.add_column(u'report_report', 'is_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True),
                      keep_default=False)

        # Adding field 'Report.photo_is_public'
        db.add_column(u'report_report', 'photo_is_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True),
                      keep_default=False)


        # Changing field 'Report.photo'
        db.alter_column(u'report_report', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=False, max_length=100))

    def backwards(self, orm):
        # Deleting field 'Report.is_public'
        db.delete_column(u'report_report', 'is_public')

        # Deleting field 'Report.photo_is_public'
        db.delete_column(u'report_report', 'photo_is_public')


        # Changing field 'Report.photo'
        db.alter_column(u'report_report', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        u'report.report': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Report'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '19'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '19'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'severity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['report']