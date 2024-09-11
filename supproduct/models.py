from django.db import models

# Create your models here.
class Suppro(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    isTrending=models.BooleanField(default=False)
    image=models.ImageField(upload_to="supproducts",blank=True)