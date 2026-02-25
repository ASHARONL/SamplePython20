from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # Enable multiple file selection

class EmailForm(forms.Form):
    recipient = forms.EmailField(label="Recipient Email")
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    attachments = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True}),
        required=False
    )

