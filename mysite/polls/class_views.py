from django.shortcuts import render
from django.views import View

class PollView(View):
    def get(self, request):
        return render(
            request,
            templete_name="polls.html",
            context={"polls":Poll.objects.all()}
        )