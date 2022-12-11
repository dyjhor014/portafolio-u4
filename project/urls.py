from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("inner", login_required(views.Inner.as_view()), name="inner"),
    path("projects/<id>", views.project, name="projects"),
    path("update_project/<id>", login_required(views.update), name="update"),
    path("update_projectinfo/", login_required(views.updated), name="updated"),
    path('registro/', views.registro, name="registro"),
    path('eliminar/<id>', views.eliminar, name="registro"),
]