import os

class Config:
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "notifications")
