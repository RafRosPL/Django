from django.urls import path
from . import views


app_name = 'users.urls'

urlpatterns = [
    path("users", UserDetailAPIView.as_view(), name="user-detail"),

]