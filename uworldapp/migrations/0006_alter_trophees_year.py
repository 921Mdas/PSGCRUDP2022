# Generated by Django 4.0.4 on 2022-04-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uworldapp', '0005_trophees_alter_performance_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trophees',
            name='year',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]