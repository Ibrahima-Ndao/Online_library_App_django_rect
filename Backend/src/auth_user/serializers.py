from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserCreateSerializier(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Choisissez les champs que vous souhaitez afficher


# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']  # Sélectionnez les champs que vous souhaitez mettre à jour
#         extra_kwargs = {
#             'email': {'required': True},  # Par exemple, rendre l'e-mail obligatoire lors de la mise à jour
#         }
