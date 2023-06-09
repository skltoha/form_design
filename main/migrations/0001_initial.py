# Generated by Django 4.0.7 on 2023-06-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('user_address', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_phone', models.CharField(max_length=20)),
            ],
        ),
    ]
