# Generated by Django 4.2.10 on 2024-02-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_post_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]