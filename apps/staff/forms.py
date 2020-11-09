from django import forms
from . import models


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        fields = ('complaint',)
        widgets = {
            'complaint': forms.Textarea(attrs={'required': True, 'rows': 1, 'class': 'form-control border-0', 'placeholder': 'Type complaints here', 'autofocus': True})
        }
