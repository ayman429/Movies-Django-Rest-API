from django.shortcuts import render
from rest_framework import viewsets
from .models import Movies
from .serializers import MoviesSerializer
# Create your views here.

class Moviesveiwsets(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
