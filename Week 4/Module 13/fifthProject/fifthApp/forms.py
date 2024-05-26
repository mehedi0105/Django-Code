from typing import Any
from django import forms
from django.core import validators


# class contactForm(forms.Form):
#     # initial="hasan",
#     #  disabled=True
#     # help_text="Total lenght must be 70 charector", required=False, widget=forms.Textarea(attrs={'placeholder': 'Enter Your Name', 'class': 'test1 test2'})
#     name = forms.CharField(label="User Name:")
#     # file = forms.FileField()
#     email = forms.CharField(label="User Email:")
#     # age = forms.IntegerField()
#     # weight = forms.FloatField()
#     # balance = forms.DecimalField()
#     # birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'Date'}))
#     # appoitment = forms.CharField(
#     #     widget=forms.DateInput(attrs={'type': 'Datetime-local'}))
#     # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Lage')]
#     # size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#     # PIZZA = [('P', 'Pepperoni'), ('M', 'Massroom'), ('B', 'Beef')]
#     # pizza = forms.MultipleChoiceField(
#     #     choices=PIZZA, widget=forms.CheckboxSelectMultiple)
#     # check = forms.BooleanField()

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name at list 10 charector")
#     #     else:
#     #         return valname

#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Youe email must contain .com")
#     #     else:
#     #         return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name at list 10 charector")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Youe email must contain .com")

def checklean(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a name at list 10 charector")


class contactForm(forms.Form):

    name = forms.CharField(label="User Name:", validators=[
                           validators.MinLengthValidator(10, message="Enter a name at list 10 charector")])
    # file = forms.FileField()
    email = forms.CharField(label="User Email:", validators=[
                            validators.EmailValidator(message="Enter a valid Email")])
    age = forms.CharField(validators=[validators.MaxLengthValidator(
        18, message="age must be Minimum 18"), validators.MinLengthValidator(34, message="age must be Maximam 34")])
    test = forms.CharField(validators=[checklean])


class passwordVarificationProject(forms.Form):
    name = forms.CharField(label="User Name:")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data['name']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password doesn't match")
