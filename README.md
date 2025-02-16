# WhatsApp Automation Tool 🚀

This **WhatsApp Automation Tool** is designed to send automated messages using **WhatsApp Desktop**. It allows you to send multiple messages from a predefined text file (`msg.txt`) to a specific phone number or a list of contacts.

---

## Features ✨
- ✅ **Automated WhatsApp Messaging**
- ✅ **Reads messages from a text file** (`msg.txt`)
- ✅ **Sends messages line by line**
- ✅ **Supports multiple recipients**
- ✅ **Uses Python and PyAutoGUI for automation**

---

## Requirements ⚙️
Ensure you have the following installed:
- **Python 3.x**
- **WhatsApp Desktop**
- **Required Python Packages**

To install dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Installation & Usage 📌

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/codervivek5/Whatsapp-Automation.git
cd Whatsapp-Automation
```

### 2️⃣ Prepare Your Message File
Create a `msg.txt` file containing the messages **(one message per line)**.

### 3️⃣ Run the Script
```bash
python main.py
```

### 4️⃣ Enter the Phone Number
The script will prompt you to enter the recipient’s **WhatsApp number**.

### 5️⃣ Messages Sent Automatically
The script will open **WhatsApp Desktop**, find the contact, and send messages **one by one**.

---

## How It Works ⚡
1. **Reads messages** from `msg.txt`
2. **Opens WhatsApp Desktop** using `webbrowser`
3. **Searches for the contact** and opens the chat
4. **Sends each message one by one**
5. **Waits between messages** to avoid spam detection

---

## Technologies Used 🛠️
- **Python** 🐍
- **PyAutoGUI** (for automation)
- **Webbrowser Module** (to open WhatsApp)

---

## Possible Enhancements 🔥
- Add AI to **generate dynamic messages**
- Implement **scheduled messaging**
- Store **contacts in a database**
- Add **GUI for easier interaction**

---

## Disclaimer ⚠️
This tool is intended **for educational purposes only**. Please ensure that you comply with **WhatsApp's terms and conditions** while using this automation.

---

## Contributing 🤝
Feel free to **fork this project** and submit **pull requests**! 🚀

For suggestions, contact: **[Vivek Kumar](https://github.com/codervivek5)**

