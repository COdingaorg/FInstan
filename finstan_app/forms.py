from django import forms
from .models import FileStat

class FileUpload(forms.ModelForm):
    class Meta:
        model = FileStat
        fields = ['__all__']
        