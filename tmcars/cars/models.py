from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='posts')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class CarCharacteristic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
