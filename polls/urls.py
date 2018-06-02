from django.urls import path

from polls.views import authorization, index

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', index.IndexView.as_view(), name='index'),
    path('login/', authorization.login, name='login'),
    path('register/', authorization.register, name='login'),
]