from django.contrib import admin
from .models import Ebooks, Links, StudyVideoLinks, StudyGuides

admin.site.register(Ebooks)
admin.site.register(Links)
admin.site.register(StudyVideoLinks)
admin.site.register(StudyGuides)