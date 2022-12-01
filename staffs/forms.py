from django import forms
from .models import Document, User
from django.contrib.auth.forms import UserCreationForm

class SendDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            "document_name",
            "recipient",
            "recipient_name",
            "document_description",
            "document_content"
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
