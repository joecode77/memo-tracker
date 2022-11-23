from django import forms
from .models import Document

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
    

