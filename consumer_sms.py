import pika
from models_contact import Contact

def send_sms(contact_id):
    # Stub function
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.sms_sent:
        print(f"Sending SMS to {contact.phone_number}")
        contact.sms_sent = True
        contact.save()

# Connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='sms_queue')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_sms(contact_id)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='sms_queue', on_message_callback=callback)
print('Waiting for SMS messages. To exit press CTRL+C')
channel.start_consuming()
