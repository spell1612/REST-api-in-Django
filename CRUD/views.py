from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import RandObject

# Create your views here.
class DisplayList(generic.ListView):
    template_name='CRUD/display.html'
    context_object_name='displist'
    def get_queryset(self):
        return RandObject.objects.all()

class DetailView(generic.DetailView):
    model=RandObject
    template_name='CRUD/details'

def enterDetails(request):
    return render(request,"CRUD/enter.html")

# def saveDetails(request):
