from django.urls import path
from . import views 

urlpatterns = [
    #Paths del core
    path('<int:page_id>/<slug:page_slug>', views.page, name='page'), #El <category_id> es una cadena de caracteres y el int se utiliza para convertirlo a numero entero
]