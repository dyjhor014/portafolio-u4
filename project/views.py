from django.shortcuts import render, redirect
from django.views import View
from .models import Project
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class IndexView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            "projects":projects
        }
        print(context)
        return render(request, "index.html", context)

class Inner(TemplateView):
    def get(self, request):
        return render(request, "inner.html")

    def post(self, request):
        photo = request.POST['photo']
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
        url = request.POST['url']
        if not photo == '' and not photo == None:
            project = Project(photo=photo, title=title, description=description, url=url, tags=tags)
            project.save()
            return redirect("index")
        return HttpResponse("No se han insertado datos")

class Login(View):
    def get(self, request):
        return render(request, "login.html")