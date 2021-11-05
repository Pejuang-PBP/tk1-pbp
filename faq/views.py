from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from faq.forms import PertanyaanLain
from faq.models import Form1, question

# Create your views here.

#@login_required(login_url="/login")
def index(request):
    tanya = Form1.objects.all()
    nanya = question.objects.all().values()
    form = PertanyaanLain(request.POST or None)
    
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
        else:
            return JsonResponse(request.POST)
            #return redirect('index')def index(request):

    # if a GET (or any other method) we'll create a blank form
    else:
        #form = PertanyaanLain()
        return render(request, "faq.html", {'form' : PertanyaanLain()}) 
    
    response = {'form': PertanyaanLain(), 'tanya':tanya, 'nanya':nanya}
    return render(request, "faq.html", response)
    


def check_question(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        pertanyaan = request.GET.get("pertanyaan", None)
        data = {
        'is_taken': Form1.objects.filter(pertanyaan__iexact=pertanyaan).exists()
    }

    return JsonResponse(data)





