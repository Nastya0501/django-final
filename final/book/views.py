from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BooksViewSet(ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = Book.objects.get(id=pk)
        serializer = BookSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Book.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = Book.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class JournalListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Journal.objects.all()
        serializer = JournalSerializer(books, many=True)
        return Response(serializer.data)


class JournalViewSet(ViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = Journal.objects.get(id=pk)
        serializer = JournalSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Journal.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = Journal.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
