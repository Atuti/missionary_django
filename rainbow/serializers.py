from .models import Question, Testimony, Prayer, Email
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'question', 'country', 'email')
    
class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ('name', 'testimony', 'country', 'email')

class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer
        fields = ('name', 'prayer', 'country', 'email')

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('name', 'message', 'number', 'email')