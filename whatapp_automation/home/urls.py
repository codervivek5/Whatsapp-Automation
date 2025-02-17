from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="send_message"),
    path("send-message/", send_message_view, name="send_message"),
]