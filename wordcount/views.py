from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def result(request):

    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    temp = []
    count = 0

    for word in wordlist:

        if word.lower() not in temp:

            count +=1
            temp.append(word.lower())

    #count = len(fulltext.split())

    return render(request, 'result.html', {'fulltext': fulltext, 'count': count})

