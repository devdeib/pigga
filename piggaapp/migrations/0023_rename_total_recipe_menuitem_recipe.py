# Generated by Django 4.2.3 on 2023-08-20 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0022_menuitem_total_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='total_recipe',
            new_name='recipe',
        ),
    ]