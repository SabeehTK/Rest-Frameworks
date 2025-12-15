from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from myapp.models import Books
from myapp.serializers import BookSerializer,UserSerializer


# Mixins API View:-

# class ViewBooks(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
#
# class ViewBookDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self, request, pk):
#         return self.update(request, pk)
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

# Generic API View:-
#
# class ViewBooks(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#
# class ViewBookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer

#Viewsets API View:-

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer