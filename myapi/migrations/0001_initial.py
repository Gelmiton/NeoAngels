# Generated by Django 3.1.14 on 2022-05-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prenatal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('mae', models.CharField(max_length=60)),
                ('cns', models.CharField(max_length=60)),
                ('unidade', models.CharField(max_length=60)),
            ],
        ),
    ]