import pika
import json
import time
from models import Contact

# Параметри підключення до RabbitMQ
rabbitmq_host = "localhost"
rabbitmq_queue = "Homework_08"

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

# Функція-заглушка для надсилання email
def send_email(contact_id):
    # Імітація надсилання email
    print(f"Надсилаємо email контакту з ID {contact_id}...")
    # Імітація часу надсилання
    time.sleep(1)  
    print(f"Email надіслано контакту з ID {contact_id}")

# Обробка повідомлень з черги RabbitMQ
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message.get("contact_id")
    
    contact = Contact.objects.filter(id=contact_id, sent=False).first()
    if contact:
        send_email(contact_id)
        contact.sent = True
        contact.save()
    else:
        print(f"Контакт з ID {contact_id} вже було оброблено.")
    
channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback, auto_ack=True)

print("Очікування повідомлень з RabbitMQ. Для виходу натисніть CTRL+C")
channel.start_consuming()