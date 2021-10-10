from django.shortcuts import render
from basic_app import views
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView, UpdateView, DeleteView)
#from django.http import HttpResponse
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School
    # From default setting, it goes to 'school_list.html'
    #template_name = "basic_app/school_list.html"

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    #Here, at default it goes to 'school.html'
    template_name = "basic_app/school_detail.html"

class SchoolCreateView(CreateView):
    #default context_object_name is 'school'
    fields = ('name', 'principal', 'location')
    model = models.School
    #From Default setting, it goes to 'school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    #default context_object_name is 'school'
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    #From Default setting, it goes to 'school_confirm_delete.html'

'''
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based Views are Great.")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Text is injected here"
        return context
'''
