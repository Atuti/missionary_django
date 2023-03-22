from rest_framework import serializers
from .models import Ebooks, Links, StudyVideoLinks, StudyGuides

class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields = ('title', 'get_ebook')

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('link','title')

class StudyVideoLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyVideoLinks
        fields = ('link', 'description')

class StudyGuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGuides
        fields = ('title', 'get_guide')