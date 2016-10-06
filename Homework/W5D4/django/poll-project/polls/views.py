from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "you didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        redirect_url = reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(redirect_url)

def add(request, question_id):
    q = Question.objects.get(pk=question_id)
    q.choice_set.create(choice_text=request.POST['add'], votes=0)
    redirect_url = reverse('polls:detail', args=(q.id,))
    return HttpResponseRedirect(redirect_url)