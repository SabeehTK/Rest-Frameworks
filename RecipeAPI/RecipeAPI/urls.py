"""
URL configuration for RecipeAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from recipes import views
from rest_framework.authtoken import views as view1

router = DefaultRouter()
router.register('recipes',views.RecipeViewSet)
router.register('users',views.UserViewSet)
router.register('reviews',views.ReviewViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search',views.Searchview.as_view()),
    path('',include(router.urls)),
    path('login/', view1.obtain_auth_token),
    path('logout', views.LogoutView.as_view()),
    path('allreviews/<int:pk>',views.AllReviews.as_view()),
]
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)