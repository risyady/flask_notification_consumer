from consumer import consume_messages

def process_sms_message(message):
    print(f"Processing SMS: {message}")

if __name__ == "__main__":
    consume_messages("SMS", process_sms_message)
