# Generated by Django 4.0.5 on 2022-07-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_delete_pessoa_delete_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='foto',
            field=models.ImageField(null=True, upload_to='images/profile/'),
        ),
    ]