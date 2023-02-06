from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ComplainForm
from .models import ComplainCategory, Region, Complaint
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


# Create your views here.

def Home(request):

    category = ComplainCategory.objects.all()
    region = Region.objects.all()

    if request.method == "POST":
        selected_cat_id = request.POST.get("category")
        selected_cat = ComplainCategory.objects.get(id=selected_cat_id)
        date = request.POST.get("date")
        description = request.POST.get("description")
        selected_reg_id = request.POST.get("region")
        selected_reg = Region.objects.get(id=selected_reg_id)

        Complaint.objects.create(
            category=selected_cat,
            date=date,
            description=description,
            region=selected_reg
        )


        return render(request, "Otify/index.html", {'category': category,
        'region': region, 'msg': "Your Complaint has been submitted successfully."})

    else:
        return render(request, "Otify/index.html", {'category': category,
        'region': region})



def Logout(request):
    logout(request)
    return render(request, "Otify/index.html")


def Login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Staff")

        else:
            messages.success(request, ("You have not been found, try again. Make sure all entered details are correct"))
            return redirect("Staff")
    else:
        return render(request, "Otify/login.html")


@login_required(login_url='Home')
def Staff(request):
    complain = Complaint.objects.all()
    return render(request, "Otify/staff.html", {'complain': complain})