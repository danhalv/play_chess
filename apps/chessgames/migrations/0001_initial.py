# Generated by Django 4.1 on 2022-08-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChessGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.CharField(choices=[('white', 'White'), ('black', 'Black')], max_length=5)),
                ('in_check', models.BooleanField()),
                ('checkmate', models.BooleanField()),
                ('board', models.JSONField()),
            ],
        ),
    ]