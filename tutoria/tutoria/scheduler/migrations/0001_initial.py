# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_hour', models.PositiveSmallIntegerField()),
                ('start_minute', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('X', 'Closed'), ('O', 'Open')], default='O', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Session'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Student'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Transaction'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Tutor'),
        ),
    ]