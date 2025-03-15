from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponse
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from django.conf import settings

def index(request):
  return HttpResponse("Hola, prueba con aplicacion de UA Day Santo Domingo")


def contact_view(request):
    error_message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simula el rechazo de correos en otros alfabetos
            correo = [form.cleaned_data['email'],]
            mensaje = form.cleaned_data['message']
            asunto = form.cleaned_data['subject']
            if "@" in correo and any(char.isdigit() for char in correo.split("@")[1]):  # Simulación de caracteres no latinos
                error_message = "❌ Nuestro servidor no acepta correos con caracteres no latinos."
            else:
                send_mail(
                    subject=asunto,auth_password=settings.EMAIL_HOST_PASSWORD,
                    message=mensaje,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=correo
                )
                return redirect("success")
    else:
        form = ContactForm()

    return render(request, "appUA/contact.html", {"form": form, "error_message": error_message})

def success_view(request):
    return render(request, 'appUA/success.html')