from twilio.rest import Client
from datetime import datetime, timedelta
import time

# twilio credentials
accout_sid = "AC6b976a039dc91a3e34457d1f0e2b45fb"
auth_token = "52e69e0b413520d8dd8db593b30db53c "

Client = Client(accout_sid, auth_token)


# sendin message
def send_whatsapp_message(recipitent_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to="whatsapp: {recipient_number}",
        )

        print(f"message sent successfully! message SID{message.sid}")
    except Exception as e:
        print("an error occured")


# user input
name = input("enter the recipient name")
recipient_number = input("enter the recipient whatsapp number with country code")
message_body = input(f"enter the message you want to send to {name}:")

# parse date time
date_str = input("enter the date to send the message(YYYY-MM-DD)")
time_str = input("enter the time to send the message (HH:MM in 24 hours format): ")

# datetime
sechedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%H-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = sechedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("the specified time is in the past. Please enter a future date and time: ")
else:
    print(f"message schedule to be sent to{name} at {sechedule_datetime}")
    # wait until the schedule time
    time.sleep(delay_seconds)

    # send the message
    send_whatsapp_message(recipient_number, message_body)
