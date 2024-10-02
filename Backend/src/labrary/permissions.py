from rest_framework.permissions import BasePermission, IsAdminUser

class IsAdminOrReadOnly(BasePermission):
    """
    La permission d'accès en lecture est accordée à tout le monde,
    tandis que les permissions d'écriture sont accordées uniquement aux administrateurs.
    """

    def has_permission(self, request, view):
        # Autorise l'accès en lecture à tout le monde
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Autorise l'accès en écriture uniquement aux administrateurs
        return request.user and request.user.is_staff
class FullAccessForAll(BasePermission):
    """
    Permet un accès complet à toutes les méthodes pour tous les utilisateurs.
    """

    def has_permission(self, request, view):
        return True