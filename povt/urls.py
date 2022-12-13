from django.urls import path
from povt import views

urlpatterns = [
    path('', views.index),
    path('create/', views.first_page),
    path('otvet/', views.otvet),
    path('get/', views.get),
    path('all/', views.TextListView.as_view()),
    path('detail/<int:pk>/', views.TextDetailView.as_view()),
]