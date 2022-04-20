# Generated by Django 2.1.7 on 2022-04-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30, null=True)),
                ('fullName', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('sum', models.CharField(max_length=50, null=True)),
                ('pageCode', models.CharField(max_length=30, null=True)),
                ('processId', models.CharField(max_length=30, null=True)),
                ('processToken', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
