import urllib

import requests
from django.conf import settings
from django.db import transaction
from django.views.generic import FormView, TemplateView
from first import first
from furl import furl

from .forms import AddHouseForm
from .models import Contract, House


class AddHouse(FormView):
    template_name = 'add_house.html'
    form_class = AddHouseForm
    success_url = '/'

    def form_valid(self, form):
        url = furl('https://maps.googleapis.com/maps/api/geocode/json')
        url.args['address'] = urllib.parse.quote_plus(form.cleaned_data['address'])
        url.args['key'] = settings.GOOGLE_MAPS_API_KEY
        resp = requests.post(url)
        resp.raise_for_status()

        latitude, longitude = first(resp.json()['results'])['geometry']['location'].values()
        with transaction.atomic():
            house = House.objects.create(
                address=form.cleaned_data['address'],
                property_type=form.cleaned_data['property_type'],
                room_count=form.cleaned_data['room_count'],
                parking_space_count=form.cleaned_data['parking_space_count'],
                lat_long=','.join([str(latitude), str(longitude)]),
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

    def get(self, request, *args, **kwargs):
        location = self.request.GET.get('location')
        if not location:
            return redirect(reverse('index'))

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        location = self.request.GET['location']
        houses = House.objects.filter(location=location)

        context = super().get_context_data(**kwargs)
        context['houses'] = houses
        return context


class Property(TemplateView):
    template_name = 'property.html'
