# Generated by Django 4.2.2 on 2023-07-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notepad', '0007_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='Text',
            field=models.CharField(default='', max_length=1000000),
        ),
    ]
