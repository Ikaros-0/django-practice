# Generated by Django 4.1 on 2023-03-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='co2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captime', models.DateTimeField()),
                ('capco2', models.CharField(max_length=10)),
            ],
        ),
    ]
