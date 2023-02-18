from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-id']