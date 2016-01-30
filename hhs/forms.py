from django import forms


class AddHouseForm(forms.Form):
    address = forms.CharField()
    property_type = forms.ChoiceField()
    room_count = forms.IntegerField()
    available_date = forms.DateField()
    price = forms.IntegerField()
    notes = forms.Textarea()
