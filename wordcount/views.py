from django.shortcuts import render
from support.tools import *

def home(request):
    return render(request, 'home.html')


def result(request):

    fulltext = request.GET['fulltext']

    result = WCTools().no_case_sensitive(fulltext.split())

    return render(request, 'result.html', {'fulltext': fulltext, 'count': result})

