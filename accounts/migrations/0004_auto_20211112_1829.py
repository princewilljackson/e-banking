# Generated by Django 3.2.7 on 2021-11-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211105_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='bank_name',
            field=models.CharField(default='gtb', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='iban_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
