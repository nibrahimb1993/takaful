# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Full name for card holder', max_length=100, verbose_name='Full Name')),
                ('phone_number', models.CharField(help_text='Phone number', max_length=15, verbose_name='Phone number')),
                ('id_number', models.CharField(help_text='ID number', max_length=10, verbose_name='ID number')),
                ('date_of_birth', models.DateField(help_text='Date of birth', verbose_name='Date of birth')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], help_text='Sex type', max_length=10, verbose_name='Sex type')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at', verbose_name='Updated at')),
                ('started_at', models.DateField(help_text='The date of start', verbose_name='Started at')),
                ('expire_at', models.DateField(blank=True, help_text='The date of expire', null=True, verbose_name='Expire at')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user who create the card', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Create by')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]