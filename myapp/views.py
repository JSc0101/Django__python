from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    # Hello world
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    # about
    return HttpResponse("<h2>About</h2>")