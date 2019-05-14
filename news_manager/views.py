from django.shortcuts import render
from .models import *

# Create your views here.
def add_preferences(request):
    providers = NewsProvider.objects.all()
    print(request.body)

    return render(request, 'add_preferences.html', {'providers':providers})