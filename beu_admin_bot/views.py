from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .bot import bot
from .forms import FoodForm
from django_tgbot.types.update import Update
from our_beu_delivery_bot.models import Restaurant as Rest,Order, Food

import logging


@csrf_exempt
def handle_bot_request(request):
    update = Update(request.body.decode("utf-8"))
    """
    All of the processing will happen in this part. It is wrapped in try-except block
    to make sure the returned HTTP status is 200. Otherwise, if your processors raise Exceptions
    causing this function to raise Exception and not return 200 status code, Telegram will stop
    sending updates to your webhook after a few tries. Instead, take the caught exception and handle it
    or log it to use for debugging later.
    """
    try:
        bot.handle_update(update)
    except Exception as e:
        if settings.DEBUG:
            raise e
        else:
            logging.exception(e)
    return HttpResponse("OK")


def poll_updates(request):
    """
    Polls all waiting updates from the server. Note that webhook should not be set if polling is used.
    You can delete the webhook by passing an empty URL as the address.
    """
    count = bot.poll_updates_and_handle()
    return HttpResponse(f"Processed {count} update{'' if count == 1 else 's'}.")

def dashboard(request, phone_num):
    rest = get_object_or_404(Rest, phone_num=phone_num)
    orders = rest.order_set.all()
    return render(request, "beu_admin_bot/orders.html", {'orders':orders, 'p':phone_num})

def accept(request, phone_num, id):
    rest = get_object_or_404(Rest, phone_num=phone_num)
    order = get_object_or_404(Order, id=id)
    order.accepted = True
    order.save()
    return HttpResponseRedirect(reverse("orders", args=[rest.phone_num,]))

def decline(request, phone_num, id):
    rest = get_object_or_404(Rest, phone_num=phone_num)
    order = get_object_or_404(Order, id=id)
    order.accepted = True
    order.save()
    return HttpResponseRedirect(reverse("orders", args=[rest.phone_num,]))

def set_prepared(request, phone_num, id):
    rest = get_object_or_404(Rest, phone_num=phone_num)
    order = get_object_or_404(Order, id=id)
    order.accepted = True
    order.save()
    return HttpResponseRedirect(reverse("orders", args=[rest.phone_num,]))

def foods(request, phone_num):
    rest = get_object_or_404(Rest, phone_num=phone_num)
    foods = rest.food_set.all()
    return render(request, "beu_admin_bot/foods.html", {'foods':foods, 'p':phone_num})

def customers(request, phone_num):
    customers = set()

    rest = get_object_or_404(Rest, phone_num=phone_num)
    for order in rest.order_set.all():
        customers.add(order.order_by)
    return render(request, "beu_admin_bot/customers.html", {'customers':list(customers), 'p':phone_num})

def add_food(request, phone_num):
    form = FoodForm()
    rest = Rest.objects.get(phone_num=phone_num)
    info = ''
    success=False
    if request.method == 'POST':
        if(form.is_valid()):
            food = Food(rest=rest)
            form=FoodForm(request.POST, instance=food)
            form.save()
            info = "New food added to database"
            success=True
        else:
            info = "Something went wrong, maybe you provided empty values !!!"


    context = {'form': form, 'info':info, 'p':rest.name, 'success':success}
    return render(request, "beu_admin_bot/add_food.html", context)


