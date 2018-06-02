from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from polls.models import Post

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(
        modifiedDate__lte=timezone.now()
    ).order_by('-modifiedDate')[:5]