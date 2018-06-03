from django.urls import path

from polls.views import authorization, index, postview

app_name = 'polls'
urlpatterns = [
    path('', index.polls, name='index'),
    path('login/', authorization.login, name='login'),
    path('register/', authorization.register, name='register'),
    path('page/', index.polls, name="page"),
    path('page/<int:page_number>/', index.polls, name="page"),
    path('post/<int:postid>/', postview.post, name="post"),
]