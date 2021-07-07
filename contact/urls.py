from django.urls import path
from . import views as core_views
from services import views as services_views
from django.conf import settings

urlpatterns = [
    #Paths del core
    path('', core_views.contact, name='contact'),
]
