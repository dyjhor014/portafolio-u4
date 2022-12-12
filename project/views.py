from django.shortcuts import render, redirect
from django.views import View
from .models import Project, Ip
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils import timezone
from .forms import CustomUserCreationFrom
from ipware import get_client_ip
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class IndexView(TemplateView):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            "projects":projects
        }
        ip, public_or_private = get_client_ip(request)
        ips = Ip(ip=ip)
        ips.save()
        return render(request, "index.html", context)

class Inner(TemplateView):
    def get(self, request):
        return render(request, "inner.html")
    @csrf_exempt
    def post(self, request):
        photo = request.POST['photo']
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
        url = request.POST['url']
        if not photo == '' and not photo == None:
            project = Project(photo=photo, title=title, description=description, url=url, tags=tags)
            project.save()
            return redirect("inner")
        return HttpResponse("No se han insertado datos")

class Login(View):
    @csrf_exempt
    def get(self, request):
        return render(request, "login.html")

@csrf_exempt
def registro(request):
    data = {
        'form': CustomUserCreationFrom
    }
    if request.method == 'POST':
        formulario = CustomUserCreationFrom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect("index")
        data['form']=formulario
    return render(request, 'registration/registro.html', data)

def project(request, id):
    project = Project.objects.get(id=id)
    context = {
            "project":project
        }
    return render(request, "projects.html", context)

def update(request, id):
    project = Project.objects.get(id=id)
    context = {
    "project":project
    }
    return render(request, "update.html", context)

def updated(request):
    id = request.POST['id']
    photo = request.POST['photo']
    title = request.POST['title']
    description = request.POST['description']
    tags = request.POST['tags']
    url = request.POST['url']
    project = Project.objects.get(id=id)
    project.photo = photo
    project.title = title
    project.description = description
    project.tags = tags
    project.url = url
    if not photo == '' and not photo == None:
        project.save()
        return redirect("index")
    return HttpResponse("No se han actualizado los datos")

def eliminar(request, id):
    project = Project.objects.get(id=id)
    project.delete_at = timezone.now()
    project.save()
    return redirect("index")