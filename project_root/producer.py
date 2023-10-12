import pika
import json
from faker import Faker
from mongoengine import connect
from models import Contact

# Підключення до  бази даних MongoDB
connect(db="mydatabase", host="localhost")

# Параметри підключення до RabbitMQ
rabbitmq_host = "localhost"
rabbitmq_queue = "Homework_08"

# Ініціалізація Faker для генерації фейкових даних
faker = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

# Генерація фейкових контактів та відправлення їх через RabbitMQ
num_contacts = 10  
for _ in range(num_contacts):
    full_name = faker.name()
    email = faker.email()
    
    # Збереження контакту в базі даних
    contact = Contact(full_name=full_name, email=email)
    contact.save()
    
    # Відправлення ідентифікатора контакту через RabbitMQ
    message = {"contact_id": str(contact.id)}
    channel.basic_publish(exchange="", routing_key=rabbitmq_queue, body=json.dumps(message))

print(f"{num_contacts} контактів було згенеровано та відправлено.")
connection.close()