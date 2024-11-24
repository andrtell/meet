from django.urls import path

from . import views

urlpatterns = [
    path("session", views.session_dump, name="debug_session_dump"),
    path("session/set/<key>/<val>", views.session_put, name="debug_session_put"),
    path("session/del/<key>", views.session_del, name="debug_session_del"),
]
