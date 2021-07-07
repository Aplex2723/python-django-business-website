from django.shortcuts import render
from .models import Project

# Create your views here.
def services(request):
    services = Project.objects.all()
    return render(request, 'core/services.html', {'services': services})