from django import forms
from website.models import Contact, Newsletter

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = Newsletter
        fields = '__all__'