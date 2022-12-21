# Generated by Django 4.1.4 on 2022-12-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natjecanje_naslov', models.CharField(max_length=100)),
                ('natjecanje_opis', models.TextField()),
                ('natjecanje_vrijeme', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
