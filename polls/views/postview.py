from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from  django.shortcuts import  render

def index(request):
    return HttpResponse("Hello Myzhiki")

from django.shortcuts import render, get_object_or_404

from polls.models import Post
from  polls.models import Candidate



def post(request, postid):
    mypost = get_object_or_404(Post, pk=postid)
    candidate_list = Candidate.objects.filter(postId=mypost.id)
    context = {'mypost':mypost,
               'candidate_list': candidate_list }
    return render(request, 'polls/post.html', context)


