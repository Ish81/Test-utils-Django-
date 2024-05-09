# # I have created this File - Ishaan
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
# #    lol = {'name':'Ishaan', 'place':'Pune'}
#    return render(request, 'index.html')
#     # return HttpResponse("Home")

# def analyze(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')

#     # Check checkbox value
#     removepunc=request.GET.get('removepunc','off')
#     fullcaps=request.GET.get('removepunc','off')

#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)

#     elif(fullcaps=="on"):
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper

#         params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
    
#     else:
#         return HttpResponse('Error')
    

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
#     return HttpResponse("char count")



# def about(request):
#     return HttpResponse("About Ishaan")

# def Google(request):
#     return HttpResponse('<p><a href="https://www.google.com/">Google</a></p>')

# def Flipkart(request):
#     return HttpResponse('<p><a href="https://www.flipkart.com/">Flipkart</a></p>')

# def Codechef(request):
#     return HttpResponse('<p><a href="https://www.codechef.com/dashboard">CodeChef</a></p>')


#  COPY PASTING HARRY CODE CASUE ERROR RESOLVE NAHI HO RAHA 
# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (removepunc != "on" and fullcaps !="on" and extraspaceremover!="on" and newlineremover != "on"):
        return HttpResponse("Error")
    # elif (charactercount == "on"):
    #     count=0
    #     for char in djtext:
    #         if char.isalpha():
    #             count = count+1

        params = {'purpose': 'Chacter count', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

