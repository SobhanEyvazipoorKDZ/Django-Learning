from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()
           messages.add_message(request, messages.SUCCESS, 'your ticket has submitted successfully.')
       else:
           messages.add_message(request, messages.ERROR, 'your ticket has some problems.')     
       return render(request, 'website/contact.html', {'form': form})
    else:
       form = ContactForm()
       return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
       form = NewsletterForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
           #messages.add_message(request, messages.SUCCESS, 'your ticket has submitted successfully.')
       else:
           return HttpResponseRedirect('/')
           #messages.add_message(request, messages.ERROR, 'your ticket has submitted successfully.')