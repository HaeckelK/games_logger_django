# Generated by Django 3.1.5 on 2021-01-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20210107_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='games.GenreCategory'),
        ),
    ]
