from finstan_app.forms import FileStatement
from django.shortcuts import render, redirect
from django.contrib import messages

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
    form = FileStatement()
    if request.method == 'POST' and 'statement_upload' in request.POST:
        form = FileStatement(request.POST, request.FILES)
        if form.is_valid():
            if request.user:
                form.user = request.user
            else:
                form.user = None

            form.save()
            messages.success(request, 'Upload successfull')
            return redirect('report')
        else:
            messages.warning(request, 'Invalid Form')
    else:
        context = {
            'title':title,
            'disclaimer':desclaimer,
            'form':form,
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
