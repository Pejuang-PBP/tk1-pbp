from django.shortcuts import render

from faq.forms import PertanyaanLain

# Create your views here.

def index(request):
    form = PertanyaanLain(request.POST or None)
        # check whether it's valid:
        # if this is a POST request we need to process the form data
    if (form.is_valid() and request.method == 'POST'):
            # process the data in form.cleaned_data as required
            # save if valid
        form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PertanyaanLain()
    response = {'form': form}
    return render(request, "faq.html", response) #response


