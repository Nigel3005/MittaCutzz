# Generated by Django 3.0.8 on 2022-01-28 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_remove_contact_achternaam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='voornaam',
            new_name='name',
        ),
    ]
