# Generated by Django 4.2.10 on 2024-02-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
