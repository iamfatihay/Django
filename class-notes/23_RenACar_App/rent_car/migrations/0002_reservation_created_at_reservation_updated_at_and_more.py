# Generated by Django 4.2.4 on 2023-08-23 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent_car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='car',
            name='plate_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='rent_per_day',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
