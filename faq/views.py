from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from faq.forms import PertanyaanLain
from faq.models import Form1

# Create your views here.

def index(request):
    form = PertanyaanLain(request.POST or None)
        # check whether it's valid:
        # if this is a POST request we need to process the form data
    if (form.is_valid() and request.method == 'POST'):
            # process the data in form.cleaned_data as required
            # save if valid
        form.save()
        #return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PertanyaanLain()
    response = {'Form1': Form1}
    return render(request, "faq.html", response) #response


