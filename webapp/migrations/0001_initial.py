# Generated by Django 4.0.1 on 2022-02-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_id', models.IntegerField()),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
            ],
        ),
    ]
