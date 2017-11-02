from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question


def index(request):
    all_questions = Question.objects.order_by('-pub_date')
    all_categories = []
    for i in all_questions:
        if i.category not in all_categories:
            all_categories.append(i.category)
    all_categories.sort()
    context = {'all_questions': all_questions, 'all_categories': all_categories}
    return render(request, 'polls/index.html', context)


def categories(request, q_category):
    context = {'q_category': q_category, 'all_questions': Question.objects.order_by('-pub_date')}
    return render(request, 'polls/category.html', context)


def detail(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    
