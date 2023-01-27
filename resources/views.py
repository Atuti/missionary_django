from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ebooks
from .serializers import EbooksSerializer

@api_view(['GET'])
def get_all_ebooks(request):
    ebooks = Ebooks.objects.all()

    serializer = EbooksSerializer(ebooks, many=True)

    return Response(serializer.data)