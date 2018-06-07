from django.db.models import Count
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from polls.models import Post
from  polls.models import Candidate
from  polls.models import User_Candidate


def post(request, postid):
    mypost = get_object_or_404(Post, pk=postid)
    candidate_user_list = Candidate.objects.filter(postId=mypost.id)
    candidate_count_list = candidate_user_list.values('candidateId').annotate(dcount=Count('postId'))
    print(candidate_count_list)
    #count = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).order_by('dcount').last()['dcount']
    #most_popular_posts_id = User_Candidate.objects.values('postId').annotate(dcount=Count('postId')).filter(
     #   dcount=count).values('postId')
    #most_popular_posts = Post.objects.filter(pk__in=most_popular_posts_id)

    context = {'mypost': mypost,
               'candidate_list': candidate_user_list,
               'username': auth.get_user(request).username}
    return render(request, 'polls/post.html', context)


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



