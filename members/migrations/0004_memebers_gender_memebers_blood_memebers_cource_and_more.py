# Generated by Django 4.2.4 on 2023-10-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_memebers_about_us_remove_memebers_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memebers',
            name='Gender',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='memebers',
            name='blood',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='memebers',
            name='cource',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='memebers',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='memebers',
            name='entry',
            field=models.TextField(null=True),
        ),
    ]
