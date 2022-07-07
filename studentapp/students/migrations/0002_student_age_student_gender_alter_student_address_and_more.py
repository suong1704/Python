# Generated by Django 4.0.3 on 2022-05-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]