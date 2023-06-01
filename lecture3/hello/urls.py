from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str: name>", views.greet, name="name"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")
    
]
