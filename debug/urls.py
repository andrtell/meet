from django.urls import path

from . import views

app_name = "debug"

urlpatterns = [
    path("session", views.session_dump, name="session_dump"),
    path("session/set/<key>/<val>", views.session_put, name="session_put"),
    path("session/del/<key>", views.session_del, name="session_del"),
]
