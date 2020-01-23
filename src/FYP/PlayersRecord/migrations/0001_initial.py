# Generated by Django 3.0 on 2020-01-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerImage', models.CharField(max_length=200)),
                ('playerFlag', models.CharField(max_length=200)),
                ('playerName', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('goalScored', models.CharField(max_length=200)),
                ('attempts', models.CharField(max_length=200)),
                ('matchPlayed', models.CharField(max_length=200)),
                ('totalPasses', models.CharField(max_length=200)),
                ('yellowCards', models.CharField(max_length=200)),
                ('RedCards', models.CharField(max_length=200)),
            ],
        ),
    ]
