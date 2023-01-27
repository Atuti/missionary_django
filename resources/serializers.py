from rest_framework import serializers
from .models import Ebooks

class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields = ('title', 'get_ebook')