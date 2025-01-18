from plyer import notification
import time

title = 'Hi, Hello and Hi !'

message = 'IAgent M! My mission to you is: Smile, dance, and conquer the day with laughter! This message will disappear in a few seconds... or maybe it wont! 😎🕶️💼🎉✨'

try:
    # Send the notification
    notification.notify(
        title=title,
        message=message,
        timeout=15,
        toast=False
    )
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for 1 hour (60 * 60 seconds)
time.sleep(60 * 60)
