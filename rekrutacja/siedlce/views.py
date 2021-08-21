from django.shortcuts import render
from django.view import View
from models import User
from django.http import JsonResponse


class UsersDetailApiView(View):
    def get(self, request):
            users = User.objects.all().values('name', 'age')
            users_list = list(questions)
            return JsonResponse({"users":users_list})


class UserDetailApiView(View):
    def get(self,request):
        try:
            users = User.objects.all().values('name', 'age')
        except User.DoesNotExist:
            response_data = {
                "status":"error",
                "message":"User/users doesnt exist"
                             }
        else:
            response_data = {
                "name": users.name,
                "age": users.age,
            }
        return JsonResponse(response_data)


class UserAddApiView(View):
    def post(selfself,request):
        body = request.POST
        name = body["name"]
        age = body["age"]
        u = User.objects.create(name=name, age=age)
        return JsonResponse({"id": u.id}, status=201)

