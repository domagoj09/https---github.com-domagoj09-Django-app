# Generated by Django 4.1.4 on 2022-12-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_sudionik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_ime', models.CharField(max_length=30)),
                ('prof_prezime', models.CharField(max_length=30)),
                ('prof_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
