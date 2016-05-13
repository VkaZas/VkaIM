from django.db import models

# Create your models here.
from account.models import User


class Message(models.Model):
    text = models.TextField('Message Content')
    send_user = models.ForeignKey(User, related_name='sent_message')
    receive_user = models.ForeignKey(User, related_name='received_message')
    send_time = models.DateTimeField('Send Time', auto_now_add=True)
    receive_flag = models.BooleanField('Received')

    def __str__(self):
        return self.text
