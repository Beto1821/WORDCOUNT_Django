# from django.http import HttpResponse
import operator
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'text': 'work on it!!!'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    fulltextsize = len(fulltext)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedword = sorted(
        worddictionary.items(),
        key=operator.itemgetter(1),
        reverse=True
        )

    return render(request, 'count.html', {
        'fulltext': fulltext,
        'wordcount': len(wordlist),
        'fulltextsize': fulltextsize,
        'worddictionary': sortedword,
        })
