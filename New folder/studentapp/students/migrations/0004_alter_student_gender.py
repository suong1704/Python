# Generated by Django 4.0.3 on 2022-04-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(default=True),
        ),
    ]
