# Generated by Django 4.2.5 on 2023-09-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp_question', '0007_remove_question_math_opt_for1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_math',
            name='correct_option',
            field=models.CharField(default='', max_length=1),
        ),
    ]
