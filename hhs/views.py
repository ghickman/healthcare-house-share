from django.db import transaction
from django.views.generic import FormView, TemplateView

from .forms import AddHouseForm
from .models import Contract, House


class AddHouse(FormView):
    template_name = 'add_house.html'
    form_class = AddHouseForm
    success_url = '/'

    def form_valid(self, form):
        with transaction.atomic():
            house = House.objects.create(
                address=form.cleaned_data['address'],
                property_type=form.cleaned_data['property_type'],
                room_count=form.cleaned_data['room_count'],
                parking_space_count=form.cleaned_data['parking_space_count'],
            )

            Contract.objects.create(
                house=house,
                user=self.request.user,
                price=form.cleaned_data['price'],
                end_date=form.cleaned_data['available_date'],
            )
        return super().form_valid(form)


class Home(TemplateView):
    template_name = 'index.html'


class Search(TemplateView):
    template_name = 'search.html'


class Property(TemplateView):
    template_name = 'property.html'
