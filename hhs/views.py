from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'

class Search(TemplateView):
    template_name = 'search.html'

class Property(TemplateView):
    template_name = 'property.html'
