# Generated by Django 4.0.3 on 2022-03-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=10)),
                ('name', models.TextField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
