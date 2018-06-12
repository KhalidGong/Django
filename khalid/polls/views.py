from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Choice,Question

def home(request):
    return render(request,'polls/home.html',{})

def media(request,media_id):
    media_list=['/root/Django/khalid/polls/file/',media_id]
    media_file=''.join(media_list)
    with open(media_file,'rb') as med:
        return HttpResponse(med,content_type="")

def show(request,imag_id="back.jpg"):
    imag=''.join(['http://106.15.179.96:8000/polls/media/',imag_id,'/'])
    return render(request,'polls/show.html',{'imag':imag})

def show2(request):
    return render(request,'polls/show2.html')

def show3(request):
    return render(request,'polls/show3.html')

def show4(request,imag_id="back.jpg"):
    imag=''.join(['http://106.15.179.96:8000/polls/media/',imag_id,'/'])
    return render(request,'polls/show4.html',{'imag':imag})

def show5(request):
    return render(request,'polls/show5.html',{})

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError ,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice.",})
    else:
        selected_choice.votes=F('votes')+1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
