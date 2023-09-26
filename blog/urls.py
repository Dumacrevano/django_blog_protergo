from django.urls import path 

from . import views

urlpatterns = [
    path('<slug:slug>/', views.detail, name='post_detail')#slug probably only reach this level that is why need to put here
]
