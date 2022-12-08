from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("inner", login_required(views.Inner.as_view()), name="inner"),
]