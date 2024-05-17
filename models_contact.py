from mongoengine import Document, StringField, BooleanField, connect

# Connect to your MongoDB Atlas database
connect('your_database_name', host='mongodb://localhost:27017/')


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)  # Added field
    preferred_contact_method = StringField(required=True, choices=["email", "sms"])  # Added field
    email_sent = BooleanField(default=False)
    sms_sent = BooleanField(default=False)
