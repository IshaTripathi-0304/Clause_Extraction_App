from django import forms
from crt.models import EBooksModel

class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = ('title', 'pdf',)