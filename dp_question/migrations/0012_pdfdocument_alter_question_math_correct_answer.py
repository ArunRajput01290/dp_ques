# Generated by Django 4.2.5 on 2023-09-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp_question', '0011_alter_question_math_correct_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
        migrations.AlterField(
            model_name='question_math',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=1),
        ),
    ]