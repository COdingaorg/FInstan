from django import forms
from .models import FileStat

class FileStatement(forms.ModelForm):
    class Meta:
        model = FileStat
        fields = ['file_path']