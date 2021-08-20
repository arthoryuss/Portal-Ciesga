from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def saiba_mais(request):
    return render(request, 'saiba_mais.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = ContactForm()
    else:
        form = ContactForm()
    context['form'] = form
    template_name = 'contact.html'
    return render(request, template_name, context)