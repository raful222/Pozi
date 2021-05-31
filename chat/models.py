from django.contrib.auth.models import User
from django.db import models
from datetime import date, timedelta

# Create your models here.
from django.db.models import Max

feel_today = (('good', "GOOD"), ('bad', "Bad"), ('excellent', "Excellent"), ('okay', "Okay"))


class chat_first_question_model(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Corona_feeling = models.CharField(max_length=5000)
    if_psychologist = models.CharField(max_length=5000)
    about_yourself = models.CharField(max_length=5000)
    feel = models.CharField(max_length=9, choices=feel_today, null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)


class payment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=9)
    card_number = models.CharField(max_length=16)
    validity = models.CharField(max_length=9)
    back_dig = models.CharField(max_length=3)
    payment_date = models.DateTimeField(auto_now_add=True, null=True)

    # gil_take1 = payment_date + timedelta(days=7)

    def __str__(self):
        return str(self.user)

    def get_paimnet(self):
        return payment.objects.all()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    body = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def send_message(from_user, to_user, body):
        sender_message = Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True)
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            body=body,
            recipient=from_user, )
        recipient_message.save()
        return sender_message

    def get_messages(user):
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
        users = []
        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
            })
        return users


class Message_cost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cost')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_cost')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_cost')
    body_cost = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def send_message(from_user_cost, to_user_cost, body_cost):
        sender_message = Message_cost(
            user=from_user_cost,
            sender=from_user_cost,
            recipient=to_user_cost,
            body_cost=body_cost,
            is_read=True)
        sender_message.save()

        recipient_message = Message_cost(
            user=to_user_cost,
            sender=from_user_cost,
            body_cost=body_cost,
            recipient=from_user_cost, )
        recipient_message.save()
        return sender_message

    def get_messages(user):
        messages = Message_cost.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by(
            '-last')
        users = []
        for message in messages:
            users.append({
                'user_cost': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message_cost.objects.filter(user=user, recipient__pk=message['recipient'],
                                                      is_read=False).count()
            })
        return users


class tip_model(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject


class QA_model(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject
