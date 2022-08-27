from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home),
    path('test/', views.Test),
    path('result/', views.Result)
]
