# Generated by Django 4.0.3 on 2022-11-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=15)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField()),
                ('total', models.TimeField()),
            ],
        ),
    ]
