from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import JsonResponse

from faq.forms import PertanyaanLain
from faq.models import Form1

# Create your views here.

def index(request):
    tanya = Form1.objects.all()
    form = PertanyaanLain(request.POST or None)
        # if this is a POST request we need to process the form data
    if (form.is_valid()):
            # save if valid
        form.save()
        #return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PertanyaanLain()
    response = {'form': form, 'tanya':tanya}
    response = {'Form1': Form1}
    return render(request, "faq.html", response) #response


def check_question(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        pertanyaan = request.GET.get("pertanyaan", None)
        # check for the nick name in the database.
        # if Form1.objects.filter(pertanyaan = pertanyaan).exists():
        #     # if nick_name found return not valid new friend
        #     return JsonResponse({"valid":False}, status = 200)
        # else:
        #     # if nick_name not found, then user can create a new friend.
        #     return JsonResponse({"valid":True}, status = 200)
        data = {
        'is_taken': Form1.objects.filter(pertanyaan__iexact=pertanyaan).exists()
    }

    return JsonResponse(data)





