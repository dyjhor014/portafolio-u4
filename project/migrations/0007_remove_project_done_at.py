# Generated by Django 4.1.4 on 2022-12-11 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='done_at',
        ),
    ]
