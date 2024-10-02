from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_due_date = models.DateField()

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
