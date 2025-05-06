from django.http import HttpResponse


def blog(request):
    print(request)
    return HttpResponse('blog do app amo a giovanda')