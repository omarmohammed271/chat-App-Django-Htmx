from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import ChatGroup,ChatMessage
from .forms import ChatMessageForm
# Create your views here.
def home(request):

    return render(request,'home.html')

@login_required
def chatting(request,chat_room = 'Clinc'):
    chat_group = get_object_or_404(ChatGroup,group_name=chat_room)
    chat_messages = chat_group.chat_messages.all()
    if request.headers.get('Hx-Request'):
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group_chat=chat_group
            message.save()
        
        context = {
            'message':message,
            'user':request.user
        }
        return render(request,'chat_message_p.html',context)
    form = ChatMessageForm()
    context = {
        'messages':chat_messages,
        'form':form,
    }
    return render(request,'chat.html',context)