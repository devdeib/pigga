# Generated by Django 4.2.3 on 2023-08-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0015_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
