import urllib

import requests
from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
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

        location = first(resp.json()['results'])['geometry']['location']
        with transaction.atomic():
            house = House.objects.create(
                address=form.cleaned_data['address'],
                property_type=form.cleaned_data['property_type'],
                room_count=form.cleaned_data['room_count'],
                parking_space_count=form.cleaned_data['parking_space_count'],
                latitude=location['lat'],
                longitude=location['lng'],
            )

            Contract.objects.create(
                house=house,
                user=self.request.user,
                price=form.cleaned_data['price'],
                end_date=form.cleaned_data['available_date'],
            )

        messages.info(self.request, 'House added!')

        return super().form_valid(form)


class Home(TemplateView):
    template_name = 'index.html'


class Search(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        location = self.request.GET.get('location')
        if not location:
            return redirect('/')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        location = self.request.GET['location']
        url = furl('https://maps.googleapis.com/maps/api/geocode/json')
        url.args['address'] = urllib.parse.quote_plus(location)
        url.args['key'] = settings.GOOGLE_MAPS_API_KEY
        resp = requests.post(url)
        resp.raise_for_status()

        location = first(resp.json()['results'])['geometry']['location']

        sql = """
        SELECT *
        FROM hhs_house
        WHERE earth_box(ll_to_earth(%s, %s), %s) @> ll_to_earth(hhs_house.latitude, hhs_house.longitude);
        """
        radius = '8046.72'  # 5 miles in metres
        houses = House.objects.raw(sql, [location['lat'], location['lng'], radius])

        context = super().get_context_data(**kwargs)
        context['houses'] = houses
        return context


class Property(TemplateView):
    template_name = 'property.html'
