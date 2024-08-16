from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        # Check if the user is authenticated and if they've already made a contact request for this listing
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id, email=email).exists()
            if has_contacted:
                messages.error(request, 'You have already made a request for this listing.')
                return redirect(f'/listings/{listing_id}')

        # Save the contact request
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()

        # Attempt to send the email
        # try:
        #     send_mail(
        #         subject='Property Listing Inquiry',
        #         message=f'There has been an inquiry for the listing "{listing}". Sign into the admin panel for more info.',
        #         from_email='test.from.amir@gmail.com',
        #         recipient_list=[realtor_email, 'amirhosseine13579@gmail.com'],
        #         fail_silently=False,
        #     )
        #     messages.success(request, f"Your request was sent to the realtor successfully. Thank you for your patience, dear {name}.")
        # except ValidationError as e:
        #     messages.error(request, 'Failed to send email. Please try again later.')
        #     print(f"Error sending email: {e}")

        return redirect(f'/listings/{listing_id}')
