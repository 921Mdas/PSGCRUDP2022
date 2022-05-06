# Generated by Django 4.0.4 on 2022-04-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField(default=60)),
                ('stamina', models.IntegerField(default=90)),
                ('passing', models.IntegerField(default=7)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=100)),
                ('language', models.CharField(choices=[('Select a language', 'Select a language'), ('French', 'French'), ('English', 'English'), ('Spanish', 'Spanish'), ('Portuguese', 'Portuguese')], default='Select a language', max_length=50)),
                ('position', models.CharField(choices=[('Select a position', 'Select a position'), ('Middlefield', 'Middlefield'), ('Striker', 'Striker'), ('Goalkeeper', 'Goalkeeper'), ('Reserve', 'Reserve')], default='Select a position', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Player',
            },
        ),
    ]