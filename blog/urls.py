from django.urls import path
from . import views 

urlpatterns = [
    #Paths del core
    path('', views.blog, name='blog'),
        #Path de las categorias
    path('category/<int:category_id>/', views.category, name='category'), #El <category_id> es una cadena de caracteres y el int se utiliza para convertirlo a numero entero
]