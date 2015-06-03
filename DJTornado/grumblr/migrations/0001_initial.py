# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grumbl',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=42)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrumblerUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_user', models.CharField(max_length=50)),
                ('followers', models.ManyToManyField(related_name=b'user_followers', to='grumblr.GrumblerUser')),
                ('following', models.ManyToManyField(related_name=b'following_users', to='grumblr.GrumblerUser')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
