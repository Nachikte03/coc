from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('bookingform/',views.bookingform,name='bookingform'),
    path('confirm/',views.confirm,name='confirm'),
    path('checkbooking/',views.checkbooking,name='checkbooking'),
    path('payment/',views.payment,name='payment'),
    path('cancelbooking/',views.cancelbooking,name='cancelbooking'),
    path('changeseat/',views.changeseat,name='changeseat'),
    path('livelocation/',views.livelocation,name='livelocation'),
    path('terms/',views.terms,name='terms'),
]
    