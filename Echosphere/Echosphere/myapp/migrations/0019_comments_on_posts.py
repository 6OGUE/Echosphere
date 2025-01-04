# Generated by Django 4.2.10 on 2024-02-26 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments_on_Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register')),
            ],
        ),
    ]
