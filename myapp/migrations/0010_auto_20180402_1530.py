# Generated by Django 2.0.2 on 2018-04-02 07:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180402_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmstring',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 2, 7, 30, 49, 579704, tzinfo=utc)),
        ),
    ]
