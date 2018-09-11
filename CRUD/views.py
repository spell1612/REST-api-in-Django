from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import datetime

from .models import RandObject
from .forms import Prod

# Create your views here.
class DisplayList(generic.ListView):
    template_name='CRUD/display.html'
    context_object_name='displist'
    def get_queryset(self):
        return RandObject.objects.all()

class DetailView(generic.DetailView):
    model=RandObject
    template_name='CRUD/details.html'

def enterDetails(request):
    #if request is POST we process this as form submitted data
    if request.method=='POST':
        # create a form instance and populate it with data from the request:
        fvar=Prod(request.POST)
        #check if form data valid
        if fvar.is_valid():
            #process data from fvar.cleaned_data
            obj=RandObject() #remember the parentheses here. Paranthesis= an instance. while no parenthesis is the actual function
            obj.objectname=fvar.cleaned_data["name"]
            obj.price=fvar.cleaned_data["price"]
            obj.save()
            return HttpResponseRedirect(reverse('CRUD:disp'),)
        else:
            #if any fields are unfilled
            return render(request,'CRUD/enter.html',{'form':fvar,'error':"All fields are mandatory"})
    else:
        fvar=Prod()
    return render(request,'CRUD/enter.html',{'form':fvar})

def editDetails(request,id):
    r=get_object_or_404(RandObject,pk=id)
    if request.method=='POST':
        f=Prod(request.POST,initial={'name':r.objectname,'price':r.price})
        if f.is_valid():
            r.objectname=f.cleaned_data["name"]
            r.price=f.cleaned_data["price"]
            r.date_added=datetime.now()
            r.save()
            return HttpResponseRedirect(reverse('CRUD:disp'),)
        else:
            return render(request,'CRUD/edit.html',{'form':f,'error':"All fields are mandatory"})
    else:
        f=Prod(initial={'name':r.objectname,'price':r.price})
    return render(request,'CRUD/edit.html',{'form':f,'id':id})
