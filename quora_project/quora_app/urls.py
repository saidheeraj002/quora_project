# qa/urls.py (Create this file)
from django.urls import path
from . import views

app_name = 'quora_app'

urlpatterns = [
    path('', views.login, name='login'), # Homepage: List questions
    path('home', views.question_list, name="home"),
    path('registration', views.register_view, name="registration"),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),  # View a question
    path('ask_question/', views.ask_question, name='ask_question'),  # Page to ask a question
    path('answer/<int:question_id>/', views.add_answer, name='add_answer'),  # POST route to add answer
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('logout', views.logout, name='logout')
    # path('question/<int:question_id>/', views.question_detail, name='question_detail'), # View a question
    # path('ask/', views.ask_question, name='ask_question'), # Page to ask a question
    # path('answer/<int:question_id>/', views.add_answer, name='add_answer'), # POST route to add answer
    # path('like/<int:answer_id>/', views.like_answer, name='like_answer'), # POST route to like/unlike
    # path('signup/', views.signup, name='signup'), # User registration page
    # Note: Login and Logout are handled by django.contrib.auth.urls included in the main urls.py
]