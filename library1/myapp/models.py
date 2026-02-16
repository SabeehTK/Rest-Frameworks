from django.db import models

# Create your models here.
class Books(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    pages=models.IntegerField()
    language=models.CharField(max_length=100)
    def __str__(self):
        return self.title

