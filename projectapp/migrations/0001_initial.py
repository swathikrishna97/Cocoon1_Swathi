# Generated by Django 4.0 on 2021-12-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('re_password', models.CharField(default='', max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
