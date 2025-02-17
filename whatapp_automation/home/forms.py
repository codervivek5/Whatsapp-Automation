from django import forms

class WhatsAppForm(forms.Form):
    phone_number = forms.CharField(label="Phone Number", max_length=15)
    message = forms.CharField(label="Message", widget=forms.Textarea)
