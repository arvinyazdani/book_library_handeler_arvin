from django.contrib.auth import urls
from . import views
from django.urls import path, include

app_name = "users"

urlpatterns = [

    path("", include(urls), name=urls),
    path("register/", views.register, name="register"),

]