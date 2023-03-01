from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest, menu_item: str='') -> HttpResponse:
    """Returns index page"""
    return render(request, "main_page/index.html")
