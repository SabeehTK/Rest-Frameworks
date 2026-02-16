from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from app1.serializers import NoteSerializer,UserSerializer
from app1.models import Note
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Searchview(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')#gets the query from the client side
                                                     #using keyname
        if query:
            b=Note.objects.filter(Q(title__icontains=query)|
                                  Q(content__icontains=query))

            if not b.exists():
                return Response({'msg': 'No results'}, status=status.HTTP_400_BAD_REQUEST)
            book=NoteSerializer(b,many=True)
            return Response(book.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg':'No results'},status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logged out successfully'},status=status.HTTP_200_OK)