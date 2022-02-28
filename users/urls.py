# from django.conf.urls import url
from django.urls import path, include
from users.views import dashboard

urlpatterns = [
    # url(r'^dashboard/', dashboard, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name='dashboard'),
]
