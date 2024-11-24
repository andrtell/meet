from django.urls import path

from . import views

urlpatterns = [
    path("", views.view, name="session_info_view"),
    path("set/<key>/<val>", views.do_set),
    path("del/<key>", views.do_del),
]
