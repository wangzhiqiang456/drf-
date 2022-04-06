from rest_framework import serializers
from k.models import BookInfo


class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'