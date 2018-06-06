from __future__ import print_function
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import render_to_response, render
from polls.models import Post, User_Candidate, Candidate
from django.core.paginator import Paginator, EmptyPage
from django.contrib import auth
from django.db.models import Count
from polls.views import postview
from django.shortcuts import render, get_object_or_404
import random
from django.template.context_processors import csrf




def polls(request, page_number=1):
    template_name = 'polls/poll_summary.html'
    try:
        all_polls = Post.objects.all().order_by('-modifiedDate')
        current_page = Paginator(all_polls, 5)
        return render_to_response(template_name, {'post_list' : current_page.page(page_number), 'username': auth.get_user(request).username, 'link': '/polls/page'})
    except( EmptyPage ):
        return render(request, template_name)

def popular(request, page_number=1):
    template_name = 'polls/poll_summary.html'
    count = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).order_by('dcount').last()['dcount']
    most_popular_posts_id = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).filter(dcount=count).values('postId')
    most_popular_posts = Post.objects.filter(pk__in=most_popular_posts_id)
    current_page = Paginator(most_popular_posts, 5)
    return render_to_response(template_name, {'post_list' : current_page.page(page_number), 'username': auth.get_user(request).username, 'link': '/polls/popular/page'})


def unpopular(request, page_number=1):
    template_name = 'polls/poll_summary.html'
    count = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).order_by('dcount').first()['dcount']
    most_unpopular_posts_id = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).filter(dcount=count).values('postId')
    most_unpopular_posts = Post.objects.filter(pk__in=most_unpopular_posts_id)
    current_page = Paginator(most_unpopular_posts, 5)
    return render_to_response(template_name, {'post_list' : current_page.page(page_number), 'username': auth.get_user(request).username, 'link': '/polls/popular/page'})


def random_poll(request):
    mypost = random.choice(Post.objects.all())
    candidate_list = Candidate.objects.filter(postId=mypost.id)
    context = {'mypost':mypost,
               'candidate_list': candidate_list ,
               'username': auth.get_user(request).username}
    return render(request, 'polls/post.html', context)


def add(request):
    args = {}
    args.update(csrf(request))
    if auth.get_user(request).is_anonymous:
        return render_to_response('polls/login.html', args)
    else:
        return render(request, 'polls/addPost.html', {'username': auth.get_user(request).username})
