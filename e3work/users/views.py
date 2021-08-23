from users.models import Users
from rest_framework import permissions, viewsets
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
