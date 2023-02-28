from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    """.REPONSE"""
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    """.About"""
    return HttpResponse("<h2>About</h2>")