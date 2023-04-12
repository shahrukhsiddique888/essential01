from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from . models import notes
# Create your views here.

class ModelView(TemplateView):
    template_name = "home/welcome.html"

class ModelListView(ListView):
    model = notes
    template_name = "home/list.html"
    context_object_name= 'don'

class ModelDetailView(DetailView):
    model = notes
    template_name = "home/details.html"
    context_object_name ='note'







