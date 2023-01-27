from django.contrib import admin
from .models import Question, Testimony, Prayer

# Register your models here.
admin.site.register(Question)
admin.site.register(Testimony)
admin.site.register(Prayer)
