# Generated by Django 4.2.5 on 2023-09-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp_question', '0008_question_math_correct_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_math',
            name='correct_option',
        ),
        migrations.AddField(
            model_name='question_math',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=1),
        ),
    ]