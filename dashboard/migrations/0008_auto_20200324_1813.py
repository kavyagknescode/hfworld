# Generated by Django 2.2.11 on 2020-03-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidatedetails',
            options={'verbose_name_plural': 'CandidateDetails'},
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name_plural': 'UserDetails'},
        ),
        migrations.AddField(
            model_name='candidatedetails',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
