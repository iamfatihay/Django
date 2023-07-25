# Generated by Django 4.2.3 on 2023-07-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_api.path')),
            ],
        ),
    ]
