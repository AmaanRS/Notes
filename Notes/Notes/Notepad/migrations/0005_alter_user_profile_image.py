# Generated by Django 4.2.2 on 2023-07-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notepad', '0004_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='Image',
            field=models.ImageField(default='Notepad/default_user_img.png', upload_to='Notes/Notes/media/Notepad'),
        ),
    ]
