# Generated by Django 2.2.11 on 2020-03-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200319_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='resume',
            field=models.FileField(help_text='Upload PDF File Only', upload_to='candidate/%Y/%m/'),
        ),
    ]