import pika
import json
import faker
from mongoengine import connect
from models import Contact

# Connect to MongoDB
connect('my_database', host='mongodb://localhost:27017')

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts')

fake = faker.Faker()

# Generate fake contacts
contacts = []
for _ in range(10):
    contact = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'sent_email': False  # Logical field indicating if the email has been sent
    }
    contacts.append(contact)

# Save contacts to MongoDB and publish messages to RabbitMQ
for contact in contacts:
    contact_obj = Contact(**contact)
    contact_obj.save()

    channel.basic_publish(exchange='', routing_key='contacts', body=json.dumps({'contact_id': str(contact_obj.id)}))

print("Contacts generated and published to RabbitMQ.")
connection.close()
