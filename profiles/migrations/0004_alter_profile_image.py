# Generated by Django 3.2.16 on 2023-03-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../blank_avatar_n8ebz9', upload_to='images/'),
        ),
    ]
