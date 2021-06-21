from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
 
# Create your views here.
def index(request):
  context = {
  "variable" : "Aditya Is A Greate Person",
  "variable1" : "Aditya Is A Greate Man"
  }
  
  return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
 if request.method == "POST":
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    qus = request.POST.get('qus')
    contact = Contact(name = name, phone = phone, email = email, qus = qus, date = datetime.today())
    contact.save()
    messages.success(request, 'User has been registered successfully.')
    return redirect('/')
 return render(request, 'contact.html')
