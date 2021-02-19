from django.shortcuts import render

# Create your views here.
from .models import Category


def index(request):
    categories=Category.objects.all()
    return render(request, 'Base.html',{'categories':categories})
    manager


