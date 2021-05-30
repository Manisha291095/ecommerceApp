from django import forms
from app1.models import Customer


class DetailsForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    city=forms.CharField()
    address=forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    Password = forms.CharField(max_length = 12)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'