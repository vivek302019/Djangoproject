# I have created this website - vivek

from django.http import HttpResponse
from django.shortcuts import render

# Code for video 7

def index(request):
    #params = {'name':'vivek','place': 'Mars'}
    return render(request,'index.html')

    #return HttpResponse("Home")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        print(djtext)
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext =analyzed
        #return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if(charcount == "on"):
        analyzed = 0
        for char in djtext:
            if char !=" ":
                analyzed = analyzed+1

        params = {'purpose': 'charcount', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)

    #else:
    #    return HttpResponse("Error")
    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

'''def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount ")'''