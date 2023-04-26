from rest_framework import serializers
from .models import Ebooks, SabbathArchiveVideoLinks, StudyToShowVideoLinks, StudyGuides, Tracts, Events

class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields = ('title', 'get_ebook')

class SabbathArchiveVideoLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SabbathArchiveVideoLinks
        fields = ('get_link','title')

class StudyToShowVideoLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyToShowVideoLinks
        fields = ('get_link', 'description')

class StudyGuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGuides
        fields = ('title', 'get_guide')

class TractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracts
        fields = ('title', 'get_tract')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'info', 'get_image', 'date')

