from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .forms import AddHouseForm


class AddHouse(FormView):
    template_name = 'add_house.html'
    form_class = AddHouseForm
    success_url = reverse_lazy('/')


class Home(TemplateView):
    template_name = 'index.html'
