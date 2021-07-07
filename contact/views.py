from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST) #Relleno de campos automaticamente
        if contact_form.is_valid(): #Comprovando si los campos son correctos
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviamos el correo y redireciconamos
            email = EmailMessage(
                "La Caffetteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["Ereson.27@hotmail.com"],
                reply_to=[email]
            )

            try:
                #si tidi va bien
                email.send()
                return redirect(reverse('contact' + "?ok"))
            except:
                #algo no ha ido bien, se redireccioina a FAIL
                return redirect(reverse('contact') + "?fail") #El request obtiene automaticamente la url c/contact/

    return render(request, 'contact/contact.html', {'form':contact_form})