import json
from mongoengine import connect
from models import Author, Quote

# Connect to the MongoDB database
connect('mydatabase', host='localhost', port=27017)

# Import authors data
def import_authors():
    with open('authors.json', 'r') as f:
        authors_data = json.load(f)
    
    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

# Import quotes data
def import_quotes():
    with open('quotes.json', 'r') as f:
        quotes_data = json.load(f)
    
    for quote_data in quotes_data:
        author_name = quote_data.pop('author')
        author = Author.objects(fullname=author_name).first()
        if author:
            quote_data['author'] = author
            quote = Quote(**quote_data)
            quote.save()

if __name__ == "__main__":
    import_authors()
    import_quotes()
    print("Data imported successfully.")
