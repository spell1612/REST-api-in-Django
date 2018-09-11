from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

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





# def saveDetails(request):
