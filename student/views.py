from django.shortcuts import render

from student.models import Image

# Create your views here.


def index(request):
    obj = Image.objects.all()
    return render(request, 'index.html', {'obj': obj})
