# Generated by Django 4.2.10 on 2024-02-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_post_likes_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.IntegerField(default=0, null=True),
        ),
    ]