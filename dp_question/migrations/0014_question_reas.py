# Generated by Django 4.2.5 on 2023-09-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp_question', '0013_question_computer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_reas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_no', models.IntegerField()),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('solution', models.CharField(default='', max_length=100)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=1)),
            ],
        ),
    ]
