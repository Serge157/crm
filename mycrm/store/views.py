from django.shortcuts import render
from .models import Flower

def home(request):
    flowers = Flower.objects.all()
    return render(request, 'store/flowers.html', {'flowers': flowers})
