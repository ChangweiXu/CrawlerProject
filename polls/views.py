# from django.shortcuts import render

# Create your views here.

# ver.1
'''
from django.http import HttpResponse

from .models import Question

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)
# end def
'''

# ver.2
from django.http import HttpResponse, Http404, HttpResponseRedirect
'''
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
# end def
'''

# ver.3
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
    	'latest_question_list': latest_question_list,
    }
    # context = {'data_one': 10, 'data_two': 2, 'data_thr': 0}
    return render(request, 'polls/index.html', context)
# end def


'''
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
# end def
'''

# ver.4
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
# end def
'''

# ver.5
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
# end def


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)
# end def

from django.urls import reverse

def vote(request, question_id):
	# return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # end try/else

# end def
