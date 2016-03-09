from django.http import HttpResponse


def index(request):
    return HttpResponse("I don't like put \"Hello world\" in here")