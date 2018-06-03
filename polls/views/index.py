from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import render_to_response, render
from polls.models import Post
from django.core.paginator import Paginator, EmptyPage

def polls(request, page_number=1):
    template_name = 'polls/poll_summary.html'
    try:
        all_polls = Post.objects.all().order_by('-modifiedDate')
        current_page = Paginator(all_polls, 5)
        return render_to_response(template_name, {'post_list' : current_page.page(page_number)})
    except( EmptyPage ):
        return render(request, template_name)