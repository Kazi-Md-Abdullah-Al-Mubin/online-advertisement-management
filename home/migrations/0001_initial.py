# Generated by Django 2.0.5 on 2018-08-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=30)),
                ('os', models.CharField(max_length=20)),
                ('browser', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=30)),
                ('site_type', models.CharField(max_length=40)),
            ],
        ),
    ]