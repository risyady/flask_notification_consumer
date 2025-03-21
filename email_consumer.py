from consumer import consume_messages

def process_email_message(message):
    print(f"Processing email: {message}")

if __name__ == "__main__":
    consume_messages("EMAIL", process_email_message)
