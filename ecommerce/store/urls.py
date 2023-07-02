from django.urls import path
from .views import *

urlpatterns = [
    path('', store , name='store'),
    path('cart/', cart , name='cart'),
    path('checkout/', checkout , name='checkout'),
    path('updateItem/', updateItem , name='updateItem'),
    path('processOrder/', processOrder , name='processOrder'),
    path('login/', login, name = 'login'),
    path('registration/', registration, name = 'registration'),
    path('logout/',logout_view, name = 'logout'),
    path('search/', search, name='search'),
]