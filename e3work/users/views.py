from Django.e3work.users.models import Users
from rest_framework import permissions, viewsets
from Django.e3work.users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
