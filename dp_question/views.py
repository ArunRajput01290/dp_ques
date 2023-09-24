from django.shortcuts import render, redirect
from .models import Card , Contact, Question_math, PDFDocument , Question_computer

def index(request):
    card = Card.objects.all()
    return render(request, 'index.html', {'card': card})
    # return render(request, 'index.html')

def contact(request):
    if request.method == "POST":  # Use "POST" in uppercase
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('Suggestion', '')  # Use the correct field name
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')


def gk(request):
    return render(request, 'gk.html')

def about(request):
    return render(request, 'about.html')


def math(request):
    question_math = Question_math.objects.all()
    return render(request, 'math.html', {'question_math': question_math})

def computer(request):
    question_computer = Question_computer.objects.all()
    return render(request, 'computer.html', {'question_computer': question_computer})

def reasoning(request):
    return render(request, 'reasoning.html')

def gk(request):
    pdf_documents = PDFDocument.objects.all()
    return render(request, 'gk.html', {'pdf_documents': pdf_documents})


def calculate_results(request):
    if request.method == 'POST':
        # Get all questions from the database
        questions = Question_math.objects.all()

        # Get the user's selected answers from the form
        user_answers = [request.POST.get(f'q{question.q_no}_option', '') for question in questions]

        # Get the correct answers from the database
        correct_answers = [question.correct_answer for question in questions]

        # Calculate the score
        score = sum(user_answer == correct_answer for user_answer, correct_answer in zip(user_answers, correct_answers))

        not_attempted = len(questions) - len([ans for ans in user_answers if ans])  # Count unanswered questions

        # Calculate the difference
        questions_attempted = len(questions) - not_attempted

        # Pass all data to the result template
        return render(request, 'result.html', {'score': score, 'not_attempted': not_attempted, 'questions': questions, 'questions_attempted': questions_attempted})
    else:
        # Handle GET request if needed
        return redirect('/')


def calculate_results_com(request):
    if request.method == 'POST':
        # Get all questions from the database
        questions = Question_computer.objects.all()

        # Get the user's selected answers from the form
        user_answers = [request.POST.get(f'q{question.q_no}_option', '') for question in questions]

        # Get the correct answers from the database
        correct_answers = [question.correct_answer for question in questions]

        # Calculate the score
        score = sum(user_answer == correct_answer for user_answer, correct_answer in zip(user_answers, correct_answers))

        not_attempted = len(questions) - len([ans for ans in user_answers if ans])  # Count unanswered questions

        # Calculate the difference
        questions_attempted = len(questions) - not_attempted

        # Pass all data to the result template
        return render(request, 'result.html', {'score': score, 'not_attempted': not_attempted, 'questions': questions, 'questions_attempted': questions_attempted})
    else:
        # Handle GET request if needed
        return redirect('/')


# def calculate_results_reas(request):
#     if request.method == 'POST':
#         # Get all questions from the database
#         questions = Question_reas.objects.all()

#         # Get the user's selected answers from the form
#         user_answers = [request.POST.get(f'q{question.q_no}_option', '') for question in questions]

#         # Get the correct answers from the database
#         correct_answers = [question.correct_answer for question in questions]

#         # Calculate the score
#         score = sum(user_answer == correct_answer for user_answer, correct_answer in zip(user_answers, correct_answers))

#         not_attempted = len(questions) - len([ans for ans in user_answers if ans])  # Count unanswered questions

#         # Calculate the difference
#         questions_attempted = len(questions) - not_attempted

#         # Pass all data to the result template
#         return render(request, 'result.html', {'score': score, 'not_attempted': not_attempted, 'questions': questions, 'questions_attempted': questions_attempted})
#     else:
#         # Handle GET request if needed
#         return redirect('/')


