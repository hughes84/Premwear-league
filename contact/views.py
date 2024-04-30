from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm


def contact_us(request):
    """
    Render the contact us page and handle contact form submissions.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered contact us page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                contact.user = request.user
            contact.save()
            # Save form data to variables
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            subject = 'New Contact Form Submission'
            message_body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            sender_email = email
            recipient_email = settings.DEFAULT_FROM_EMAIL

            send_mail(subject, message_body, sender_email, [recipient_email])
            messages.success(request,
                             'Your message has been sent successfully!')

            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})
