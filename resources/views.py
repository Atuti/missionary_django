from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ebooks, SabbathArchiveVideoLinks, StudyToShowVideoLinks, StudyGuides, Tracts, Events
from .serializers import EbooksSerializer, SabbathArchiveVideoLinksSerializer, StudyToShowVideoLinksSerializer, StudyGuidesSerializer, TractsSerializer, EventsSerializer

@api_view(['GET'])
def get_all_ebooks(request):
    ebooks = Ebooks.objects.all()

    serializer = EbooksSerializer(ebooks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_first_ebook(request):
    ebook = Ebooks.objects.all()[:1].get()

    serializer = EbooksSerializer(ebook)

    return Response(serializer.data)

@api_view(['GET'])
def get_links(request):
    links = SabbathArchiveVideoLinks.objects.all()

    serializer = SabbathArchiveVideoLinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_home_links(request):
    links = SabbathArchiveVideoLinks.objects.all().order_by('-date_filed')[:3]

    serializer  = SabbathArchiveVideoLinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_study_links(request):
    links = StudyToShowVideoLinks.objects.all()

    serializer = StudyToShowVideoLinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_study_guides(request):
    guides = StudyGuides.objects.all()

    serializer = StudyGuidesSerializer(guides, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_all_tracts(request):
    tracts = Tracts.objects.all()

    serializer = TractsSerializer(tracts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_events(request):
    events = Events.objects.all().order_by('-date')

    serializer = EventsSerializer(events, many=True)

    return Response(serializer.data)