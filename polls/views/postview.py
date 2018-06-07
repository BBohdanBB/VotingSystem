from django.db.models import Count
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from  polls.models import Candidate, User_Candidate, Post
from django.contrib.auth.decorators import login_required

from django.template.defaulttags import register

@register.filter
def lookup(d, key):
    return d[key]

def post(request, postid):
    mypost = get_object_or_404(Post, pk=postid)
    candidate_votes = {a: 0 for a in Candidate.objects.filter(postId=postid)}
    for c_u in User_Candidate.objects.filter(postId=postid):
        candidate_votes[c_u.candidateId]+=1
    context = {'mypost': mypost,
               'username': auth.get_user(request).username,
               'candidate_votes': candidate_votes, }
    return render(request, 'polls/post.html', context)

@login_required
def vote(request, postid):
    post = get_object_or_404(Post, pk=postid)
    selected_candidate = post.candidate_set.get(pk=request.POST['choice'])
    user_post = User_Candidate.objects.filter(userId=request.user.id).filter(postId=post.id)
    if user_post.count() > 0:
        return render(request,'polls/message.html', {'message': 'You have already voted'} )
    user_cand = User_Candidate.objects.create()
    user_cand.postId = post
    user_cand.candidateId = selected_candidate
    user_cand.userId = request.user
    user_cand.save()
    return render(request,'polls/message.html', {'message': 'Thank you! You vote for  ' + user_cand.candidateId.name})



