# Generated by Django 4.2.2 on 2023-06-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time', models.DateTimeField()),
                ('customer', models.TextField()),
                ('types', models.BooleanField()),
            ],
        ),
    ]
