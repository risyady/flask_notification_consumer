import pika
import json
from config import Config

def get_rabbitmq_connection():
    params = pika.URLParameters(Config.RABBITMQ_URL)
    return pika.BlockingConnection(params)

def consume_messages(service_name, callback):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    # Pastikan exchange ada
    channel.exchange_declare(exchange=Config.EXCHANGE_NAME, exchange_type='fanout', durable=True)

    # Deklarasi antrean unik
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Bind ke exchange
    channel.queue_bind(exchange=Config.EXCHANGE_NAME, queue=queue_name)

    print(f"[{service_name}] Listening for messages...")

    def on_message(ch, method, properties, body):
        message = json.loads(body)
        print(f"[{service_name}] Received: {message}")
        callback(message)

    channel.basic_consume(queue=queue_name, on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()
