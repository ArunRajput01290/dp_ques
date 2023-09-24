from django.contrib import admin

# Register your models here.
from. models import Card , Contact, Question_math, PDFDocument ,Question_computer
admin.site.register(Card)
admin.site.register(Contact)
admin.site.register(Question_math)
admin.site.register(PDFDocument)
admin.site.register(Question_computer)
