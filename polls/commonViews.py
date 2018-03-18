from django.views import generic
from polls.models import Question,Choice

'''
    两个通用视图：
    ListView 显示一个对象列表
    DetailView 显示一个特定类型对象的详细信息页面
    
    DetailView期望从URL中捕获名为"pk"的主键值，
    因此我们把polls/urls.py中question_id改成了pk以使通用视图可以找到主键值 
    
    
'''
class IndexView(generic.ListView):
    template_name = 'index3.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('pubDate')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request,pk):
    pass