# Generated by Django 4.2.2 on 2023-08-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0006_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='purpose',
            field=models.TextField(),
        ),
    ]