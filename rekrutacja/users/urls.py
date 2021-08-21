from django.urls import path
from . import views


app_name = 'users.urls'

urlpatterns = [
    path("users/<pk>/", views.UserDetailAPIView.as_view(), name="user-detail"),
    path("users/add/", views.UserAddAPIView.as_view(), name="user-add")

]