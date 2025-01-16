from django.shortcuts import render

# Create your views here.

def landingpage(request):
    data = {
        "title": "Accueil",
    }
    return render(request, "landingpage.html", data)

def login(request):
    data = {
        "title": "Login",
    }
    return render(request, "login.html", data)

def qcm(request):
    data = {
        "title": "Qcm",
    }
    return render(request, "qcm.html", data)