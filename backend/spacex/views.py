from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext


def coverage(request):
    page_view = 'htmlcov/index.html'

    return render(request, page_view)