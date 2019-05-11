from django.urls import path
from codeScanner import views

app_name = "codeScanner"

urlpatterns = [
    path('', views.scanCode, name='codeScanner'),
    path("add/<code>", views.add, name="add"),
    path("show/<code>", views.show, name="show"),
]