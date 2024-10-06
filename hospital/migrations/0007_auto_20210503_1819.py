# Generated by Django 2.2.13 on 2021-05-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_bloodordermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodordermodel',
            name='bloodtype',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B+', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10, null=True),
        ),
    ]
