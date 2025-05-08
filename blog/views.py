from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    print(request)
    return HttpResponse('blog do app amo a giovanda')

def exemplo(request):
    print('exemplo')
    return render(request, 'blog/exemplo.html')