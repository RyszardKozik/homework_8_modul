from mongoengine import Document, StringField, ListField, ReferenceField, connect

# Connect to your MongoDB Atlas database
connect('your_database_name', host='mongodb://localhost:27017/')


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
