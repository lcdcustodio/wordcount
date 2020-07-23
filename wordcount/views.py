from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def result(request):

    fulltext = request.GET['fulltext']
    count = len(fulltext.split())

    return render(request, 'result.html', {'fulltext': fulltext, 'count': count})

