# Generated by Django 3.2.7 on 2021-11-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211104_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationaltransfer',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Declined', 'Declined')], default='Successful', max_length=20),
        ),
        migrations.AlterField(
            model_name='localtransfer',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Declined', 'Declined')], default='Successful', max_length=20),
        ),
    ]
