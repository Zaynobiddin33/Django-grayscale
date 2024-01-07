from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def main(request):
    notifies = Notify.objects.all()
    context = {
        "notifies" : notifies
    }
    return render(request, "index.html", context)
