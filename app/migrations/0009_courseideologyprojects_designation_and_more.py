# Generated by Django 5.0.4 on 2024-05-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_announcement_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseideologyprojects',
            name='designation',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='courseideologyprojects',
            name='projectPerson',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courseideologyprojects',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
