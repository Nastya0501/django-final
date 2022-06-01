from rest_framework.serializers import ModelSerializer

from .models import Book, Journal


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = "__all__"
