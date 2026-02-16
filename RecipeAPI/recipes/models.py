from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='images/')
    mealtype=models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    def __str__(self):
        return self.recipe_name

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.recipe.recipe_name