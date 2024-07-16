from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import ChatGroup,ChatMessage
# Create your views here.
def home(request):

    return render(request,'home.html')

@login_required
def chatting(request,chat_room = 'Clinc'):
    chat_group = get_object_or_404(ChatGroup,group_name=chat_room)
    chat_messages = chat_group.chat_messages.all()
    context = {
        'messages':chat_messages,
    }
    return render(request,'chat.html',context)