from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from core.models import Profile


def contact_view(request):
    profile = Profile.objects.filter(is_active=True).first()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            messages.success(
                request, "Thank you for your message! I will get back to you soon."
            )
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, "contact/contact.html", {"profile": profile})
