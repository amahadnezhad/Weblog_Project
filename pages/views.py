from django.shortcuts import render
from django.views import generic


class HomeListView(generic.TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(generic.TemplateView):
    template_name = 'pages/aboutus.html'
