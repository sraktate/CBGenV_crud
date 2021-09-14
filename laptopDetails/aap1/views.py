from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Laptop

# Create your views here.

class LaptopListView(ListView):
    model=Laptop
   

class LaptopCreateView(CreateView):
    model=Laptop
    fields='__all__'
    success_url='/aap1/listview'

class LaptopUpdateView(UpdateView):
    model=Laptop
    fields='__all__'
    success_url='/aap1/listview'

class LaptopDeleteView(DeleteView):
    model=Laptop
    success_url='/aap1/listview'

def Homeview(request):
    template_name = "Home.html"
    context ={}
    return render(request,template_name,context)