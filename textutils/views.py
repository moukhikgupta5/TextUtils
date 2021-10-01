# this is user generated file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request, 'index.html')

def analyze(request):
    #Get the text
    txt = request.GET.get('text','default')
    
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremove = request.GET.get('newlineremove','off')
    extraspaceremove = request.GET.get('extraspaceremove','off')
    charcount = request.GET.get('charcount','off')

    if removepunc=='on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ch in txt:
            if ch not in punctuations:
                analyzed =analyzed+ch
        params={'purpose':'Remove Punctutaion','analyzed_text':analyzed}
    elif fullcaps=='on':
        analyzed=''
        for ch in txt:
            analyzed = analyzed + ch.upper()
        params = {'purpose':'UPPER CASE','analyzed_text':analyzed}
    elif newlineremove == 'on':
        analyzed=''
        for ch in txt:
            if ch != '\n':
                analyzed = analyzed+ch
        params = {'purpose':'Remove new line','analyzed_text':analyzed}
    elif extraspaceremove=='on':
        analyzed=''
        for i,ch in enumerate(txt):
            if not(txt[i]==" " and txt[i+1]==" "):
                analyzed = analyzed + ch
        params = {'purpose':'Remove extra space','analyzed_text':analyzed}
    elif charcount == 'on':
        analyzed = "The number of characters are "
        count=len(txt);
        # for ch in txt:
        #     if ch!=" ":
        #         count += 1
        analyzed = analyzed + str(count)
        params = {'purpose':'Count Characters','analyzed_text':analyzed}
    else:
        analyzed = txt
        params = {'purpose':'No option selected','analyzed_text':analyzed}
    return render(request, 'analyze.html',params)