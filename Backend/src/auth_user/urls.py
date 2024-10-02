from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserView
router = DefaultRouter()

# Enregistrer les ViewSets avec le routeur
router.register('users', UserView, basename='users-api')

urlpatterns = router.urls
