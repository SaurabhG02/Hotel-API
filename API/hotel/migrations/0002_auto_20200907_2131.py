# Generated by Django 2.2.12 on 2020-09-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.TextField(null=True),
        ),
    ]