from django.contrib import admin
from django.urls import include, path
from polls.views import index, authorization

urlpatterns = [
    path('', index.polls),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', authorization.login, name='login'),
]
