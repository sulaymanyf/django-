from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', context={'students': students})
