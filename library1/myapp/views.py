from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from myapp.models import Books
from myapp.serializers import BookSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status

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
    permission_classes = [IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Searchview(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')#gets the query from the client side
                                                     #using keyname
        if query:
            b=Books.objects.filter(Q(title__icontains=query)|
                                  Q(author__icontains=query)|
                                  Q(language__icontains=query)|
                                  Q(price__icontains=query))

            if not b.exists():
                return Response({'msg': 'No results'}, status=status.HTTP_400_BAD_REQUEST)
            book=BookSerializer(b,many=True)
            return Response(book.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg':'No results'},status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logged out successfully'},status=status.HTTP_200_OK)