from django.shortcuts import render , HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    context={
        "variable":"Tabish"
    }
    return render(request , "index.html", context)

def about(request):
    return render(request , "about.html")

def menu(request):
    return render(request , "menu.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_text = request.POST.get('desc')

        # Save to database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            desc=message_text,
            date=datetime.today()
        )
        contact.save()

        # Send email notification to your Gmail
        send_mail(
            subject=f"Jingle Icecream Contact Form: New Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message_text}",
            from_email='Jingle Icecream <your@gmail.com>',  # ←  important
            recipient_list=[settings.EMAIL_HOST_USER],  #your Gmail
        )

        messages.success(request, "Your message has been sent.")

    return render(request, "contact.html")
def dinein(request):
    return render(request , "dine.html")

def takeaway(request):
    return render(request , "take.html")