from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control width= 300px', 'placeholder': 'Please enter your names here'}), max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a correct email address'}), max_length=100)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your address here'}), max_length=100)
    comment = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message Here'}))
    class Meta:
        model = Contact
        fields = '__all__' 