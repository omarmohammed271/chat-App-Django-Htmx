from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'home.html')

def chatting(request):

    return render(request,'chat.html')