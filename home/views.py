from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    imagelink1 = "http://192.168.219.155/JDPP/image/Penguins.jpg"
    
    postL = Post.objects.filter(published_date__lte=timezone.now()
                        ).order_by('-published_date')[:5]

    return render(request, 'index.html', {
        'imagelink1': imagelink1,
        'postL': postL,
    })