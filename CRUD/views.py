from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
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

# def enterDetails(request):
#     #if request is POST we process this as form submitted data
#     if request.method=='POST':
#         # create a form instance and populate it with data from the request:
#         fvar=Prod(request.POST)
#         #check if form data valid
#         if fvar.is_valid():
#             #process data from fvar.cleaned_data
#             obj=RandObject() #remember the parentheses here. Paranthesis= an instance. while no parenthesis is the actual function
#             obj.objectname=fvar.cleaned_data["name"]
#             obj.price=fvar.cleaned_data["price"]
#             obj.save()
#             return HttpResponseRedirect(reverse('CRUD:disp'),)
#         else:
#             #if any fields are unfilled
#             return render(request,'CRUD/enter.html',{'form':fvar.as_p(),'error':"All fields are mandatory"})
#     else:
#         fvar=Prod()
#     return render(request,'CRUD/enter.html',{'form':fvar.as_p()})

class EnterDetails(generic.CreateView):     #generic CreateView is used to display a form based off of the model and accept inputs to the db
    form_class=Prod                             #dont need to assign model as the form class accepts a ModelForm which is already built upon a model
    template_name='CRUD/enter.html'
    success_url=reverse_lazy('CRUD:disp') #reverse_lazy() instead of reverse() as the URLconf isnt loaded yet or something

# def editDetails(request,id):
#     r=get_object_or_404(RandObject,pk=id)
#     if request.method=='POST':
#         f=Prod(request.POST,initial={'name':r.objectname,'price':r.price})
#         if f.is_valid():
#             r.objectname=f.cleaned_data["name"]
#             r.price=f.cleaned_data["price"]
#             r.date_added=datetime.now()
#             r.save()
#             return HttpResponseRedirect(reverse('CRUD:disp'),)
#         else:
#             return render(request,'CRUD/edit.html',{'form':f.as_p(),'error':"All fields are mandatory"})
#     else:
#         f=Prod(initial={'name':r.objectname,'price':r.price})
#     return render(request,'CRUD/edit.html',{'form':f.as_p(),'id':id})

class EditDetails(generic.UpdateView):
    model=RandObject    #but for some reason the model needed to be included as well here else it wasnt working
    form_class=Prod
    template_name='CRUD/enter.html'
    success_url=reverse_lazy('CRUD:disp')



# def deleteDetails(request,id):
#     r=get_object_or_404(RandObject,pk=id)
#     r.delete()
#     return HttpResponseRedirect(reverse('CRUD:disp'),)

class DeleteDetails(generic.DeleteView):
    model=RandObject
    success_url=reverse_lazy('CRUD:disp')   #The DeleteView page displayed to a GET request uses a template_name_suffix of '_confirm_delete'.
    # For example, changing this attribute to '_check_delete' for a view deleting objects for the example Author model would cause the default template_name to be 'myapp/author_check_delete.html'.
