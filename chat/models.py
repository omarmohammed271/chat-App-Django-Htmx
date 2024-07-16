from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=200,unique=True, blank=True)

    def __str__(self) -> str:
        return self.group_name

class ChatMessage(models.Model):
    group_chat = models.ForeignKey(ChatGroup, on_delete=models.CASCADE) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering = ['-created']
    
