# Generated by Django 4.1.4 on 2023-09-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='request_cost',
            field=models.FloatField(),
        ),
    ]
