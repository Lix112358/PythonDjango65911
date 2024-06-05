# Generated by Django 5.0.4 on 2024-04-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_courseideologyprojects_leaderid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseideologyprojects',
            name='projectStatus',
            field=models.CharField(choices=[('pending', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
