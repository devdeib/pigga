# Generated by Django 4.2.3 on 2023-08-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0008_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='password',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]