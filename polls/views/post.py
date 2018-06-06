from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import timezone
from django.urls import reverse
from polls.models import Post, Candidate
#from polls.forms import AddPostForm


def addPost(request):
    if request.method == "GET":
        post = Post
        candidate = Candidate
        context = {
            'post': post,
            'candidate': candidate
        }
        return render(request, 'polls/addPost.html', context)


