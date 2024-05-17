import pika
import json
import time
from models import Contact

def send_email(contact_id):
    # Simulate sending email
    print(f"Email sent to contact with ID: {contact_id}")
    # Update the sent_email field in MongoDB
    contact = Contact.objects(id=contact_id).first()
    if contact:
        contact.sent_email = True
        contact.save()

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts')

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']
    send_email(contact_id)

channel.basic_consume(queue='contacts', on_message_callback=callback, auto_ack=True)
print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
