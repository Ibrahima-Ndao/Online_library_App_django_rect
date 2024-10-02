from rest_framework.viewsets import ModelViewSet
from .models import Book, Loan
from .serializers import BookSerializer, LoanCreateSerializer, LoanDetailSerializer
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAdminOrReadOnly]


class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return LoanCreateSerializer
        return LoanDetailSerializer