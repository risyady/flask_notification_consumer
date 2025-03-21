from consumer import consume_messages

def process_fcm_message(message):
    print(f"Processing FCM: {message}")

if __name__ == "__main__":
    consume_messages("FCM", process_fcm_message)
