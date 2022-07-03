from django import forms

OPTIONS=[
    ('match','Match'),
    ('offset','Offset'),
]

class TimezoneForm(forms.Form):
    filterType = forms.CharField(label='Select the filter type',widget=forms.Select(choices=OPTIONS))
    searchString = forms.CharField()
