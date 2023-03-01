from django.http import HttpResponse

# Create your views here.


def hello_world(request, id):
    # Hello world
    print(type(id))
    return HttpResponse("<h1>Hello %s </h1>" % id)

def about(request):
    # about
    return HttpResponse("<h2>About</h2>")

def main(request):
    # index
    return HttpResponse("<h2>index page</h2>")
