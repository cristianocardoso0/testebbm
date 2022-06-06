from django.http import HttpResponse

def teste(request):
    return HttpResponse("<h1>Teste BBM</h1>")