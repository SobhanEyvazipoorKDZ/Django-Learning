from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = Newsletter
        fields = '__all__'