from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import timezone
from django.urls import reverse
from polls.models import Post, Candidate
from polls.forms import AddPostForm


def addPost(request):
    if request.method=="GET":
        return render(request, 'polls/addPost.html')
    else:
        post = AddPostForm(request.POST)
        if post.is_valid():
            post.save()
        return HttpResponse("Hui")

