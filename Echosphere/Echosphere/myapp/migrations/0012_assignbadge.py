# Generated by Django 4.2.10 on 2024-02-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badgeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.badge')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register')),
            ],
        ),
    ]
