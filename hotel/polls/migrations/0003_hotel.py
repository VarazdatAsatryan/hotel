# Generated by Django 4.2.4 on 2023-10-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_booling_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotels', models.CharField(choices=[('Ani Plaza', 'Ani Plaza'), ('Tufenkian', 'Tufnekian'), ('The Alexander', 'The Alexander')], max_length=100, null=True)),
            ],
        ),
    ]
