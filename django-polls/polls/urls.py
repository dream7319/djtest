from . import views
from django.conf.urls import url,include
from polls import formViews,commonViews

app_name='polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.demo, name= 'demo'),
    # ex: /polls/5/
    url(r'^(?P<questionId>[0-9]+)/$',views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<questionId>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<questionId>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^index3/$', views.index3, name='index3'),
    url(r'^index4/$', views.index4, name='index4'),
    url(r'^(?P<questionId>[0-9]+)/detail2/$', views.detail2, name='detail2'),
    url(r'^(?P<questionId>[0-9]+)/detail3/$', views.detail3, name='detail3'),

    url(r'^(?P<questionId>[0-9]+)/form/$', formViews.form, name='form'),

    #通用视图
    # url(r'^$', commonViews.IndexView.as_view(), name='commonIndex'),
    # url(r'^(?P<pk>[0-9]+)/$', commonViews.DetailView.as_view(), name='commonDetail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', commonViews.ResultsView.as_view(), name='commonResults'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', commonViews.vote, name='commonVotes'),
]
