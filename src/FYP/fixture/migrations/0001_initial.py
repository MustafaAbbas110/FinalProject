# Generated by Django 3.0 on 2019-12-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournment', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('HomeTeam', models.CharField(max_length=200)),
                ('AwayTeam', models.CharField(max_length=200)),
                ('HomeImage', models.CharField(max_length=200)),
                ('AwayImage', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Time', models.CharField(max_length=200)),
                ('Ground', models.CharField(max_length=200)),
                ('Attendence', models.CharField(max_length=200)),
                ('exDate', models.DateField()),
            ],
        ),
    ]
