from django.contrib import admin

from .models import Post, Candidate, User_Candidate

admin.site.register(Post)
admin.site.register(Candidate)
admin.site.register(User_Candidate)