from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

#https://stackoverflow.com/questions/17130803/include-template-as-verbatim
from django import template
from django.template.loader import get_template
from django.utils.html import escape

import os,re

def home(request):
    #return HttpResponse("<h1>Hello!</h1>")
    return render(request, 'export/ai.html', {})

def book(request,file_path):
    file = 'export/' + file_path

    #escaped file
    #template = get_template(file)
    #return HttpResponse(escape(template.render()),content_type='text/html')

    #html django template
    match_dj = re.search(".*_dj.html$",file)
    if(match_dj):
        return render(request, file, {})


    rootDir = os.getcwd()
    #from django.conf import settings
    #print(settings.BASE_DIR)    

    #local
    if(re.search(".*/pydata$",rootDir)):
        templatesLocation = "notebooks/templates/"
    #remote    
    else:
        templatesLocation = "pydata/notebooks/templates/"

    #raw html file: no rendering
    #root folder = pydata
    f = open(templatesLocation + file, mode = 'r')
    strFile = f.read()
    f.close()
    return HttpResponse(strFile,content_type='text/html')

    #just in case
    #return render(request, file, {})

def about(request):
    return render(request, 'about.html', {})

# Handle 404 Errors
def error404(request, exception):

    print("?")

    template = loader.get_template('404.html')
    context = Context({
        'message': 'All: %s' % request,
        })

    # 3. Return Template for this view + Data
    #return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

    return render(request, '404.htm', {'message': 'All: %s' % request}, status=404)
