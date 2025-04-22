from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Course, Status, StudyMatch, Message, Review

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(StudyMatch)
admin.site.register(Message)
admin.site.register(Review)
