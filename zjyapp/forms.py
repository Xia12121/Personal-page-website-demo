# Programmer: Xia Linhan
# Date: 2023.12.5

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'content']
