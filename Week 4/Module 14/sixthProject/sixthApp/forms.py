from django import forms
from sixthApp.models import StudetModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudetModel
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn-primary'}),
        }
        help_texts = {
            'name': 'Write Your Full Name: '
        }
