from django.urls import path, include
from . import views


app_name = 'quiz'

urlpatterns = [
    path('question/', views.addQuestion, name='add'), #question
    path('quiz/', views.quiz, name='quiz'), #get all questions
    path('edit/<int:id>', views.edit),  #edit question
    path('update/<int:id>', views.update), #update question
    path('delete/<int:id>', views.destroy),   #delete question
    path('edit/note/<int:id>', views.noteEdit),  #edit question
    path('update/note/<int:id>', views.noteUpdate), #update question
    
    
]
