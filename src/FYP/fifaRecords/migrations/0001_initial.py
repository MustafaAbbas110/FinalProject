# Generated by Django 3.0 on 2019-12-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomeTeam', models.CharField(max_length=200)),
                ('HomeImage', models.CharField(max_length=200)),
                ('AwayTeam', models.CharField(max_length=200)),
                ('AwayImage', models.CharField(max_length=200)),
                ('Score', models.CharField(max_length=200)),
                ('Venue', models.CharField(max_length=200)),
            ],
        ),
    ]
