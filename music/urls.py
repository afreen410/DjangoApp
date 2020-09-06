from django.urls import path
from . import views

app_name='music'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('register/', views.UserFormView.as_view(),name='register'),
    path('<pk>/',views.DetailView.as_view(),name='detail'),
     path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
     path('album/<pk>/',views.AlbumUpdate.as_view(),name='album-update'),
     path('album/<pk>/delete/',views.AlbumDelete.as_view(),name='album-delete'),
]