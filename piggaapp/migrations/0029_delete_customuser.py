# Generated by Django 4.2.3 on 2023-08-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0028_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]