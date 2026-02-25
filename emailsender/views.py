from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage, BadHeaderError
from .forms import EmailForm

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = 'your_email@gmail.com'  # Replace with EMAIL_HOST_USER

            try:
                email = EmailMessage(subject, message, from_email, [recipient])

                # Attach multiple files
                files = request.FILES.getlist('attachments')
                for f in files:
                    email.attach(f.name, f.read(), f.content_type)

                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Email with attachments sent successfully!')
    else:
        form = EmailForm()

    return render(request, 'emailsender/send_email.html', {'form': form})