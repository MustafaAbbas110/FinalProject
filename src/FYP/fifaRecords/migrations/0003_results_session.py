# Generated by Django 3.0 on 2019-12-13 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fifaRecords', '0002_results_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='Session',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]