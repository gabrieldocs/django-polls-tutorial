from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
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
    #response = 'You are looking at the results of question %s' % question_id
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question':question,
            'error_message': "You didn't selected a choice"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # redirects things
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))