from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm


# Create your views here.

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(name=name, email=email, comment=comment)
        contact.save()
        return HttpResponse('Message Sent Successfully! <a href="/">Go Back</a>')
    return render(request, 'index.html', {'form': form})

def components(request):
    return render(request, 'components.html')