from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QuestionSerializer, TestimonySerializer, PrayerSerializer
from .models import Question, Testimony, Prayer

@api_view(['POST'])
def send_question(request):
    data = request.data

    question = Question.objects.create(name = data.get('name'), country = data.get('country'), email = data.get('email'), question = data.get('question'))

    serializer = QuestionSerializer(question)

    return Response(serializer.data)

@api_view(['POST'])
def send_testimony(request):
    data = request.data

    testimony = Testimony.objects.create(name = data.get('name'), country = data.get('country'), email = data.get('email'), testimony= data.get('testimony'))

    serializer = TestimonySerializer(testimony)

    return Response(serializer.data)

@api_view(['POST'])
def send_prayer_request(request):
    data = request.data

    prayer = Prayer.objects.create(name = data.get('name'), country = data.get('country'), email = data.get('email'), prayer = data.get('prayer'))

    serializer = PrayerSerializer(prayer)

    return Response(serializer.data)
