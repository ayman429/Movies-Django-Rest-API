from django.urls import path,include
from rest_framework.routers import DefaultRouter
from movies import views

router = DefaultRouter()
router.register('',views.Moviesveiwsets)

urlpatterns = [
    path('', include(router.urls))
]