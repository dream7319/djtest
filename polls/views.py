from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
import datetime
from polls.models import Question,Choice
from django.template import RequestContext,loader
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    itemList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render_to_response("index.html", {'current_date': now, 'item_list': itemList,
                                             'infoDic': info_dict, 'ordered_warranty': True})

def demo(request):
    return render(request,"demo.html",{"current_time": datetime.datetime.now()})

def operObj(request):
    filter_startwith = Question.objects.filter(questionText__startswith='What')
    id1 = Question.objects.get(id=1)
    id1.choice_set.all()

def detail(request,questionId):
    return HttpResponse("you're looking at questions %s." % questionId)

def results(request,questionId):
    question = get_object_or_404(Question,pk = questionId)
    return render(request, "results.html", {'question' : question})

def vote(request,questionId):
    return HttpResponse("you're voting on questions %s." % questionId)

def index2(request):
    latest_question_list = Question.objects.order_by('pubDate')[:5]
    output = ','.join([p.questionText for p in latest_question_list])
    return HttpResponse(output)

def index3(request):
    #查询数据库中的数据
    latest_question_list = Question.objects.order_by('pubDate')[:5]
    template = loader.get_template("index3.html")
    return HttpResponse(template.render({
        "latest_question_list": latest_question_list,
    }))
def index4(request):
    #查询数据库中的数据
    latest_question_list = Question.objects.order_by('pubDate')[:1]
    context = {"latest_question_list": latest_question_list}
    return render(request,'index3.html',context)

def detail2(request,questionId):
    try:
        question = Question.objects.get(pk=questionId)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'detail.html', {'question': question})

def detail3(request,questionId):
    question = get_object_or_404(Question,pk=questionId)
    return render(request,'detail.html', {'question': question})

def demo1(request):
    pass
