from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    imagelink1 = "http://192.168.219.155/JDPP/image/Penguins.jpg"
    return render(request, 'index.html', {
        'imagelink1': imagelink1,
    })