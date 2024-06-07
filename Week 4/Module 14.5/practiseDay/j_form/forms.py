from django import forms
from django.forms.widgets import NumberInput


class ExampleForm(forms.Form):
    name = forms.CharField(label='Name:')
    email = forms.EmailField(label='Email:')
    date = forms.DateField(
        label='Date:', widget=NumberInput(attrs={'type': 'date'}))
    weight = forms.DecimalField(label='Weight:')
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    multipe_favorite_color = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField()
    email = forms.EmailField(
        required=False,
    )
