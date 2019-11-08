from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at result of question {}".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("you're voting on question {}".format(question_id))
