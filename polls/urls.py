from django.urls import path

from polls.views import authorization, index, postview

app_name = 'polls'
urlpatterns = [
    path('', index.polls, name='index'),
    path('login/', authorization.login, name='login'),
    path('logout/', authorization.logout, name='logout'),
    path('register/', authorization.register, name='register'),
    path('page/', index.polls, name="page"),
    path('popular/', index.popular, name="popular"),
    path('popular/page/<int:page_number>/', index.popular, name="popular"),
    path('unpopular/', index.unpopular, name="unpopular"),
    path('unpopular/page/<int:page_number>/', index.unpopular, name="unpopular"),
    path('random/', index.random_poll, name="random"),
    path('page/<int:page_number>/', index.polls, name="page"),
    path('post/<int:postid>/', postview.post, name="post"),
    path('vote/<int:postid>/', postview.vote, name='vote'),
]