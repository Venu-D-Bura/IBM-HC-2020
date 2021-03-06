# Generated by Django 3.0.8 on 2020-07-10 13:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtags',
            name='timecreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 10, 19, 17, 2, 969294)),
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
                ('neutral', models.IntegerField()),
                ('timecreated', models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 10, 19, 17, 3, 39601))),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hashtags')),
            ],
        ),
    ]
