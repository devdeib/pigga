# Generated by Django 4.2.3 on 2023-08-20 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggaapp', '0023_rename_total_recipe_menuitem_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='recipe',
            new_name='total_recipe',
        ),
    ]