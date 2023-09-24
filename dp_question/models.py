from django.db import models
class Card(models.Model):
    image = models.ImageField(upload_to='card_images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_name = models.CharField(max_length=50, default='')  # Set your desired default value

    def get_full_link_url(self):
        base_url = "http://127.0.0.1:8000/"
        return base_url + self.link_name + ".html"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Question_math(models.Model):
    q_no = models.IntegerField()
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    solution = models.CharField(max_length=100, default='')
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='')


class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')


class Question_computer(models.Model):
    q_no = models.IntegerField()
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    solution = models.CharField(max_length=100, default='')
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='')

# class Question_reas(models.Model):
#     q_no = models.IntegerField()
#     question = models.TextField()
#     option1 = models.CharField(max_length=100)
#     option2 = models.CharField(max_length=100)
#     option3 = models.CharField(max_length=100)
#     option4 = models.CharField(max_length=100)
#     solution = models.CharField(max_length=100, default='')
#     correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='')