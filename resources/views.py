from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ebooks, Links, StudyVideoLinks, StudyGuides
from .serializers import EbooksSerializer, LinksSerializer, StudyVideoLinksSerializer, StudyGuidesSerializer

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
    links = Links.objects.all()

    serializer = LinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_home_links(request):
    links = Links.objects.all().order_by('-date_filed')[:3]

    serializer  = LinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_study_links(request):
    links = StudyVideoLinks.objects.all()

    serializer = StudyVideoLinksSerializer(links, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_study_guides(request):
    guides = StudyGuides.objects.all()

    serializer = StudyGuidesSerializer(guides, many=True)

    return Response(serializer.data)