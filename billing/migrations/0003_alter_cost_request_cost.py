# Generated by Django 4.1.4 on 2023-09-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_cost_request_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='request_cost',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]