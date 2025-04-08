from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegistrationForm, QuestionForm, AnswerForm
from .models import Users, Question, Answer
from django.urls import reverse
from django.http import HttpResponseRedirect

def login(request):
    form = LoginForm()
    return render(request, "login.html", {'form': form})

def login_submit(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = Users.objects.create(username=username, password=password)
            return redirect('/')
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def question_list(request):
    """Displays a list of all questions."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = request.POST.get('username')
            questions = Question.objects.order_by('-created_at') # Latest first
            context = {'questions': questions}
            return render(request, 'question_list.html', context)
        else:
            return render(request, 'login.html', {'form': form})
    else:
        if "user" in request.session:
            questions = Question.objects.order_by('-created_at')  # Latest first
            context = {'questions': questions}
            return render(request, 'question_list.html', context)
        else:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'form': form})


def ask_question(request):
    """Handles the creation of a new question."""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = Users.objects.get(username=request.session['user'])
            question = form.save(commit=False) # Don't save to DB yet
            question.author = user
            question.save()
            return redirect('/home', question_id=question.id) # Redirect to the new question
    else: # GET request
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'ask_question.html', context)

def question_detail(request, question_id):
    """Displays a single question and its answers."""
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answers.order_by('-created_at') # Or order by likes later
    answer_form = AnswerForm() # Empty form for adding new answers

    context = {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
    }
    return render(request, 'question_detail.html', context)


def add_answer(request, question_id):
    """Handles submission of a new answer for a specific question."""
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user = Users.objects.get(username=request.session['user'])
            answer = form.save(commit=False)
            answer.author = user
            answer.question = question
            answer.save()
            return redirect('quora_app:question_detail', question_id=question.id)
        else:
            return redirect('/question_detail', question_id=question.id)
    else:
        return redirect('/question_detail', question_id=question.id)


def like_answer(request, answer_id):
    """Handles liking/unliking an answer."""
    answer = get_object_or_404(Answer, pk=answer_id)
    user = Users.objects.get(username=request.session['user'])

    if user in answer.likes.all():
        answer.likes.remove(user)
    else:
        answer.likes.add(user)

    redirect_url = request.META.get('HTTP_REFERER', reverse('quora_app:question_detail', args=[answer.question.id]))
    return HttpResponseRedirect(redirect_url)

def logout(request):
    request.session.flush()
    return redirect("/")

