# Generated by Django 4.2.4 on 2023-10-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booling',
            name='hotels',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.hotel'),
        ),
    ]
