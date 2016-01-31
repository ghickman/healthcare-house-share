from django import forms


house_type_choices = (
    ('house', 'House'),
    ('flat', 'Flat'),
)


class AddHouseForm(forms.Form):
    address = forms.CharField()
    property_type = forms.ChoiceField(choices=house_type_choices)
    room_count = forms.IntegerField()
    available_date = forms.DateField(input_formats=['%a %b %d %Y'])
    price = forms.IntegerField()
    notes = forms.CharField(widget=forms.Textarea())
