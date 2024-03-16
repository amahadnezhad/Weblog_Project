from django.shortcuts import render
from django.views import generic


class AboutUsView(generic.TemplateView):
    template_name = 'pages/aboutus.html'
