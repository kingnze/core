from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contacts(request):
   if request.method == 'POST':
      myproperty_id = request.POST['myproperty_id']
      myproperty = request.POST['myproperty']
      name = request.POST['name']
      email = request.POST['email']
      phone = request.POST['phone']
      message = request.POST['message']
      user_id = request.POST['user_id']

      contacts = Contact(myproperty=myproperty, myproperty_id=myproperty_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

      contacts.save()

      messages.success(request, 'Your request has been submited, a realtor will get back to you thanks')
      return redirect('myproperties')



      