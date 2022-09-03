from django.shortcuts import render
from .forms import CreateContactForm
from .models import ContactUs



# Create your views here.

def contact_us(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data['full_name']
        email = contact_form.cleaned_data['email']
        phone = contact_form.cleaned_data['phone']
        subject = contact_form.cleaned_data['subject']
        text = contact_form.cleaned_data['text']
        ContactUs.objects.create(full_name=full_name, email=email, phone=phone, subject=subject, text=text,
                                 is_read=False)
        # todo: show user a success message
        contact_form = CreateContactForm()
    context = {
        'contact_form': contact_form,
    }

    return render(request, 'Docusign_Contact/contact.html', context)
