from django.shortcuts import render
from django.http import HttpResponse
from crt.forms import UploadBookForm
from crt.models import EBooksModel

# Create your views here.

def home(request):
    return render(request, 'crt/home.html', {})

def new(request):
    return render(request, 'crt/new.html', {})

def BookUploadView(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'crt/UploadBook.html', context)

def show(request):
    res = EBooksModel.objects.all()
    print(res)
    return render(request, 'crt/show.html', {'res':res})