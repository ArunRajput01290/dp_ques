# Generated by Django 4.2.5 on 2023-09-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp_question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='link',
        ),
        migrations.AddField(
            model_name='card',
            name='link_name',
            field=models.CharField(default='default-link_name', max_length=50),
        ),
    ]
