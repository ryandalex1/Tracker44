# Generated by Django 3.0.8 on 2020-07-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0003_auto_20200724_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='date',
            field=models.CharField(default='June 6th, 1944', max_length=25),
            preserve_default=False,
        ),
    ]
