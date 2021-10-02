from django.shortcuts import render

def index(request):
    return  render(request, 'index.html')

def analyze(request):
    #Get the text
    txt = request.POST.get('text','default')
    
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')

    if removepunc=='on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ch in txt:
            if ch not in punctuations:
                analyzed =analyzed+ch
        txt = analyzed
    if fullcaps=='on':
        analyzed=''
        for ch in txt:
            analyzed = analyzed + ch.upper()
        txt = analyzed
    if newlineremove == 'on':
        analyzed=''
        for ch in txt:
            if ch != '\n' and ch!="\r":
                analyzed = analyzed+ch
        txt = analyzed
    if extraspaceremove=='on':
        analyzed=''
        for i,ch in enumerate(txt):
            s = len(txt)-1
            if(i<s):
                if not(txt[i]==" " and txt[i+1]==" ") :
                    analyzed = analyzed + ch
            else :
                analyzed = analyzed + ch
        txt = analyzed

    analyzed = txt
    params = {'purpose':'No option selected','analyzed_text':analyzed}
    return render(request, 'analyze.html',params)