from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Działa!. Jesteśmy w pierwszej aplikacji Django - ankiety. Gratulacje")
