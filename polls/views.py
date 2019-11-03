from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Question

# Create your views here.

# ex 1 -- show default HTML directly from function
# ex 2 -- show Questions directly from function
# ex 3 -- show Questions via loader
# ex 4 -- show Questions via render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # (2) output = ', '.join([q.question_text for q in latest_question_list])
    # (3) template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # (1) return HttpResponse('Hello, world. You\'re at the polls index.')
    # (2) return HttpResponse(output)
    # (3) return HttpResponse(template.render(context, request))
    # (4)
    return render(request, 'polls/index.html', context)

# (1) search question via try and except
# (2) search question via get_object_or_404
def detail(request, question_id):
    # (1) try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # (2)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # (1) return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)