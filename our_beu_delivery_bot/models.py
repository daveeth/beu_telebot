from django.db import models
from django.db.models import CASCADE

from django_tgbot.models import AbstractTelegramUser, AbstractTelegramChat, AbstractTelegramState


class TelegramUser(AbstractTelegramUser):
    phone_num = models.TextField()


class TelegramChat(AbstractTelegramChat):
    pass


class TelegramState(AbstractTelegramState):
    telegram_user = models.ForeignKey(TelegramUser, related_name='telegram_states', on_delete=CASCADE, blank=True, null=True)
    telegram_chat = models.ForeignKey(TelegramChat, related_name='telegram_states', on_delete=CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ('telegram_user', 'telegram_chat')


class Restaurant(models.Model):
    phone_num=models.TextField()
    name=models.TextField()

class Food(models.Model):
    name=models.CharField(max_length = 12)
    price=models.FloatField(default=0)
    rest=models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    order_by=models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null = True)
    item=models.TextField()
    accepted=models.BooleanField(default=False)
    prepared=models.BooleanField(default=False)
    quantity=models.IntegerField(default=0)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ordered_at=models.DateTimeField(auto_now_add=True)
