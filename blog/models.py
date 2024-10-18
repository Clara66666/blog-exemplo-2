from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    titulo = models.CharField(max_length=140)
    subititulo = models.CharField(max_length=140, blank=True)
    data_cricao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo