# Generated by Django 2.1.3 on 2018-11-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vip',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
