# Generated by Django 2.2.11 on 2020-03-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200326_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Subscription Price'),
        ),
    ]
