# Generated by Django 4.1.7 on 2023-05-15 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_personas_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.carrera'),
        ),
    ]
