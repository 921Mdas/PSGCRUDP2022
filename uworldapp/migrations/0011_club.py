# Generated by Django 4.0.4 on 2022-05-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uworldapp', '0010_alter_player_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('nationality', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
