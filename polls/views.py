from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]        
    context = {  'latest_question_list' : latest_question_list }    
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn's exist")
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    response = 'You are looking at the results of question %s' % question_id
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are vonting on %s' % question_id)