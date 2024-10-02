from rest_framework.serializers import CharField, ModelSerializer, ValidationError, SerializerMethodField
from .models import Book, Loan

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        


class LoanCreateSerializer(ModelSerializer):
    class Meta:
        model = Loan
        fields = ['book', 'user', 'return_due_date']

    # Validation pour s'assurer que le livre est disponible
    def validate(self, data):
        if not data['book'].available:
            raise ValidationError("Le livre sélectionné n'est pas disponible.")
        return data

    def create(self, validated_data):
        # Créer le prêt
        loan = Loan.objects.create(**validated_data)
        # Marquer le livre comme non disponible après le prêt
        loan.book.available = False
        loan.book.save()
        return loan

class LoanDetailSerializer(ModelSerializer):
    user_full_name = SerializerMethodField()
    book_title = CharField(source='book.title')
    
    class Meta:
        model = Loan
        fields = ['user_full_name', 'book_title', 'loan_date', 'return_due_date']
    
    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
