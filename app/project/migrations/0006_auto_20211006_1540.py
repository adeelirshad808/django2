# Generated by Django 3.2.7 on 2021-10-06 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20211006_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Registered account', 'verbose_name_plural': 'Registered accounts'},
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='marks',
            new_name='marks_obtained',
        ),
    ]