from win10toast import ToastNotifier
import time

# Create a ToastNotifier object
toaster = ToastNotifier()

# List of messages to be sent
messages = [
    "Hi, Hello and Hi!",
    "If you're reading this ~ I LOVE YOU TO THE MOON AND BACK!",
    "Don't forget to take a break and drink some water!",
    "You're doing great! Keep up the awesome work!"
]

# Send each message as a notification with a delay in between
for i, message in enumerate(messages):
    # Show notification
    toaster.show_toast(f"Message {i + 1}", message, icon_path=None, duration=10)
    
    # Wait for 1 second before sending the next notification
    time.sleep(1)
