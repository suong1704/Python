# Generated by Django 4.0.3 on 2022-05-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
