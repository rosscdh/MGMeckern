# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'report_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('severity', self.gf('django.db.models.fields.IntegerField')()),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=22, decimal_places=19)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(max_digits=22, decimal_places=19)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        ))
        db.send_create_signal(u'report', ['Report'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'report_report')


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
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '19'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '19'}),
            'severity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['report']