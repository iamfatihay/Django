# Generated by Django 4.2.3 on 2023-07-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationsApp', '0002_alter_profile_account_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='adress',
            field=models.TextField(null=True),
        ),
    ]
