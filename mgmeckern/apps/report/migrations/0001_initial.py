# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import mgmeckern.apps.report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('comment', models.TextField(help_text='Your review of the problem', verbose_name='Comment')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('severity', models.IntegerField(choices=[(2, 'Critical'), (1, 'Bad'), (0, 'Irritating')], default=0, help_text='How bad is the problem?', verbose_name='Severity')),
                ('report_type', models.IntegerField(choices=[(0, 'Damage'), (1, 'Improvement')], default=0, help_text='What kind of report is this?', verbose_name='Type of Report')),
                ('lat', models.DecimalField(decimal_places=19, max_digits=22)),
                ('lon', models.DecimalField(decimal_places=19, max_digits=22)),
                ('photo', models.ImageField(blank=True, help_text='Upload photographic evidence', upload_to=mgmeckern.apps.report.models._report_upload_path)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('photo_is_public', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
