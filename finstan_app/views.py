from django.shortcuts import render

# Create your views here.
#view function to index page
def index(request):
    '''
    renders index page
    '''
    title = 'Welcome to FInstan'

    context = {
        title : 'title'
    }
    return render(request, 'all_templates/index.html', context)

#View function to upload a file
def upload_file(request):
    '''
    View function to upload a file
    '''
    title = 'Upload you statement'
    desclaimer = "Your statement are safe and only when uploaded"

    context = {
        title:'title',
        desclaimer :'disclaimer'
    }

    return render(request, 'all_templates/upload_file.html', context)

#view function to view report
def report(request):
    '''
    Renders report template
    '''
    title = 'Report'
    subtext = "Here is your expense report"

    context = {
        title:'title',
        subtext :'subtext'
    }

    return render(request, 'all_templates/report.html', context)
