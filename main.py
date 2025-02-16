import webbrowser
import time
import pyautogui

def send_whatsapp_message(phone_number, message):
    # ✅ Open WhatsApp using URI
    url = f"whatsapp://send?phone={phone_number}&text={message}"
    webbrowser.open(url)
    
    # ✅ Wait for WhatsApp to open
    time.sleep(5)

    # ✅ Press "Enter" to send the message
    pyautogui.press("enter")

    print(f"✅ Message sent: {message}")
    time.sleep(3)

if __name__ == "__main__":
    phone_number = "+917393017587"  # Replace with the actual number

    # ✅ Read the file and send messages line by line
    with open("msg.txt", "r", encoding='utf-8') as file:
        
        for line in file:
            message = line.strip()  # Remove extra spaces and newlines
            if message:  # Ensure message is not empty
                send_whatsapp_message(phone_number, message)
                time.sleep(2)  # Wait before sending the next message
