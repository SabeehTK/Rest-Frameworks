from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets,status
from recipes.models import Recipe,Review
from recipes.serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q



# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Searchview(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            b=Recipe.objects.filter(Q(recipe_name__icontains=query)|
                                  Q(instructions__icontains=query)|
                                  Q(ingredients__icontains=query)|
                                  Q(mealtype__icontains=query)|
                                    Q(cuisine__icontains=query))

            if not b.exists():
                return Response({'msg': 'No results'}, status=status.HTTP_400_BAD_REQUEST)
            r=RecipeSerializer(b,many=True)
            return Response(r.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg':'No results'},status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logged out successfully'},status=status.HTTP_200_OK)

class ReviewViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class AllReviews(APIView):
    def get(self,request,pk):
        try:
            r=Recipe.objects.get(id=pk)
        except:
            raise Http404
        rev=Review.objects.filter(recipe=r)
        reviews=ReviewSerializer(rev, many=True)

        return Response(reviews.data,status=status.HTTP_200_OK)