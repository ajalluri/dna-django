from django.urls import path

from .views import get_user_data,apitesting,store_user_data
urlpatterns = [path("getuser/<str:userid>/",get_user_data),path("storeuser/<str:userid>/",store_user_data)]


#path("",apitesting),
