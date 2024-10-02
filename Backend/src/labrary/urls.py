from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet

router = DefaultRouter()

# Enregistrer les ViewSets avec le routeur
router.register('books', BookViewSet, basename='books-api')
router.register('loans', LoanViewSet, basename='loan-api')

urlpatterns = router.urls
