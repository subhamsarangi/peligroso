from django.urls import path

from . import views

app_name = 'descansa'
urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetail.as_view())
]

