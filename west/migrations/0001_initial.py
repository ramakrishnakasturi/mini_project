# Generated by Django 3.2.9 on 2022-05-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to=None)),
                ('gender', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
