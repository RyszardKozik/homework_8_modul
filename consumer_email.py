import pika
from models_contact import Contact

def send_email(contact_id):
    # Stub function
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.email_sent:
        print(f"Sending email to {contact.email}")
        contact.email_sent = True
        contact.save()

# Connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_email(contact_id)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='email_queue', on_message_callback=callback)
print('Waiting for email messages. To exit press CTRL+C')
channel.start_consuming()
