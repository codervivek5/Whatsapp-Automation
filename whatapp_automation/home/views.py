import webbrowser
import time
import pyautogui
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import WhatsAppForm


def home(request):
   return render(request , 'home.html')

def send_whatsapp_message(phone_number, message):
    #Opens WhatsApp Web and sends a message.
    
    url = f"whatsapp://send?phone={phone_number}&text={message}"
    webbrowser.open(url)
    time.sleep(1)
    pyautogui.press("enter")
    return f"✅ Message sent to {phone_number}"

def send_message_view(request):
   
   #  Handles the Django form submission and triggers WhatsApp message.
   
    if request.method == "POST":
        form = WhatsAppForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            result = send_whatsapp_message(phone, message)
            # return JsonResponse({"status": "success", "message": result})
            return redirect("send_message")
    else:
        form = WhatsAppForm()
    return render(request, "send_message.html", {"form": form})

   
