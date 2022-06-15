from django.forms import ModelForm
from our_beu_delivery_bot.models import Food

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price']