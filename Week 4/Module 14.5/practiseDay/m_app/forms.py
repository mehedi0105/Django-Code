from django import forms
from .models import MyModel


class Model_Form(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        labels = {
            'name': 'Name:',
            'email': 'Email:',
            'Url': 'Website Link:'
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'btn btn-primary'})
        # }
        help_texts = {
            'name': 'Write Your Full Name: '
        }
