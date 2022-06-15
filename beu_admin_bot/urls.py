from django.urls import path
from .views import handle_bot_request, poll_updates, dashboard, accept, decline, set_prepared, foods, customers, add_food

urlpatterns = [
    path('update/', handle_bot_request),
    path('poll/', poll_updates),
    path('dashboard/<str:phone_num>/', dashboard, name="orders"),
    path('dashboard/<str:phone_num>/orders/<int:id>/accept/', accept, name="accept"),
    path('dashboard/<str:phone_num>/orders/<int:id>/decline/', decline, name="decline"),
    path('dashboard/<str:phone_num>/orders/<int:id>/set_prepared/', set_prepared, name="set_prepared"),
    path('dashboard/<str:phone_num>/foods/', foods, name="foods"),
    path('dashboard/<str:phone_num>/customers/', customers, name="customers"),
    path('dashboard/<str:phone_num>/foods/new', add_food, name="add_food"),
]
