# Generated by Django 3.2.7 on 2021-09-17 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='screenshot',
        ),
    ]