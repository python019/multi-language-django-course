from django.db import models

# Create your models here.
class Malumot(models.Model):
    nomi = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()

    def __str__(self):
        return self.nomi