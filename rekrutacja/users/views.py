from django.shortcuts import render
from django.views import View
from users.models import User
from django.http import JsonResponse


class UserDetailAPIView(View):
    def get(self,request,pk):
        try:
            # users = User.objects.all().values('name', 'age')
            users = User.object.get(pk=pk)
        except User.DoesNotExist:
            response_data = {
                "status":"error",
                "message":"User doesnt exist"
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

