from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .serializers import AuthorSerializer
from .models import Author


class AuthorPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    filter_backends = [SearchFilter]
    search_fields = ['slug',]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

