# Generated by Django 4.2.10 on 2024-02-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]