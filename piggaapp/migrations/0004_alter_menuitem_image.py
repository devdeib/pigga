# Generated by Django 4.2.3 on 2023-07-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0003_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='', upload_to='menu_images/'),
        ),
    ]
