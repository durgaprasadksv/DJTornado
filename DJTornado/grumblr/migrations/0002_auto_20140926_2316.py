# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grumblr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrumblComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=50)),
                ('grumbl', models.ForeignKey(to='grumblr.Grumbl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrumblrUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aboutme', models.CharField(max_length=50)),
                ('blocked', models.ManyToManyField(related_name=b'blocked_users', to='grumblr.GrumblrUser')),
                ('followers', models.ManyToManyField(related_name=b'user_followers', to='grumblr.GrumblrUser')),
                ('following', models.ManyToManyField(related_name=b'following_users', to='grumblr.GrumblrUser')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='grumbleruser',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='grumbleruser',
            name='following',
        ),
        migrations.RemoveField(
            model_name='grumbleruser',
            name='user',
        ),
        migrations.DeleteModel(
            name='GrumblerUser',
        ),
        migrations.RemoveField(
            model_name='grumbl',
            name='image',
        ),
        migrations.AddField(
            model_name='grumbl',
            name='dislikes',
            field=models.ManyToManyField(related_name=b'dislikes', to='grumblr.GrumblrUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grumbl',
            name='likes',
            field=models.ManyToManyField(related_name=b'likes', to='grumblr.GrumblrUser'),
            preserve_default=True,
        ),
    ]
