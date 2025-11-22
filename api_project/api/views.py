from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewset
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewset.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self,request, *args, **kwargs):
        book = self.get_serializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data)

    def list(self,request):
        serialized = BookSerializer(self.queryset,many=True)
        return Response(serialized.data)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(self.queryset,pk=pk)
        serialized = BookSerializer(book)
        return Response(serialized.data)

    def update(self, request, *args, **kwargs):
        book = self.get_object()
        serialize = self.get_serializer(
            book,
            data=request.data,
            partial=True
        )
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response("Book deleted")