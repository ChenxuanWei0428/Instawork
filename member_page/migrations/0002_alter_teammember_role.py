# Generated by Django 4.2.7 on 2023-12-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Admin', 'Admin')], default='Regular', max_length=100),
        ),
    ]
