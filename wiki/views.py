from django.shortcuts import render

# Create your views here.
def wikiview(r):
    return render(r,'wiki/wiki.html')