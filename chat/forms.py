from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields=['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'common-input', 'maxlength' : '300', 'autofocus': True }),
        }
# common-input
# p-4 text-black