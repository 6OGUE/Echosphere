# Generated by Django 4.2.10 on 2024-02-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_register_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='type',
            field=models.CharField(default='pending', max_length=100, null=True),
        ),
    ]