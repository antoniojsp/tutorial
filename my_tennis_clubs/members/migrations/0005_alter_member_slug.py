# Generated by Django 4.1.5 on 2023-01-29 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
