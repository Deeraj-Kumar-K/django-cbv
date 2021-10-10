from django.shortcuts import render
from basic_app import views
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
'''
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based Views are Great.")
'''

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Text is injected here"
        return context
