# Generated by Django 3.0 on 2019-12-13 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fifaRecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='Group',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
