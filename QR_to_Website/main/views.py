from operator import imod
from re import template
from unittest import TestProgram
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.core.mail import EmailMessage
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from .models import doctor_name,doctor_details
from django.template.loader import render_to_string


def home(request):
    if request.method=="POST":
        doc=doctor_name()
        doc.name=request.POST.get('name2')

        doc.save()
        doc_name=request.POST.get('name2')


        mail(doc_name)
        return render(request, 'main/qr_code_generated.html')
    return render(request, 'main/home.html')

def mail(nam):
    qr_code=doctor_name.objects.get(name=nam)
    template=render_to_string('main/mailpage.html', {'content':qr_code})
    email = EmailMessage(
                'Thank you for registering to our site',
                template,
                settings.EMAIL_HOST_USER,
                ['ramucm130@gmail.com',],
            )

    email.fail_silently=False

    email.send()

def doctor_page(request,pk):
    
    try:
        content=doctor_name.objects.get(name=pk)
        if request.method=="POST":
            doc=doctor_details()
            doc.name=pk
            doc.phone=request.POST.get('phone')
            doc.save()
            return render(request, 'main/doc_details_saved.html')
        return render(request, 'main/doctor_page.html',{'content':content})
    except:
        return render(request, 'main/404.html')
    



    