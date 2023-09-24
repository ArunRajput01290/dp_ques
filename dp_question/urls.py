from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('contact.html', views.contact, name="Home"),
    path('about.html', views.about, name="Home"),
    path('math', views.math, name="Home"),
    path('gk', views.gk, name="Home"),
    path('reasoning', views.reasoning, name="Home"),
    path('computer', views.computer, name="Home"),
    path('calculate_results/', views.calculate_results, name='calculate_results_math'),
    path('calculate_results_com/', views.calculate_results_com, name='calculate_results_computer'),
    # path('calculate_results_reas/', views.calculate_results_reas, name='calculate_results'),
]