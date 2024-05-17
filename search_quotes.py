from models import Quote

def search_quotes(query):
    # Search by tag, author's name, or set of tags
    if query.startswith("name:"):
        author_name = query.split("name:")[1].strip()
        quotes = Quote.objects(author__fullname__icontains=author_name)
    elif query.startswith("tag:"):
        tag = query.split("tag:")[1].strip()
        quotes = Quote.objects(tags__icontains=tag)
    elif query.startswith("tags:"):
        tags = query.split("tags:")[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
    else:
        return "Invalid query format."

    # Format the search results
    results = []
    for quote in quotes:
        results.append(f"{quote.author.fullname}: {quote.quote}")
    
    return results

if __name__ == "__main__":
    while True:
        query = input("Enter search query (name:, tag:, tags:) or 'exit' to quit: ")
        if query == "exit":
            break
        results = search_quotes(query)
        for result in results:
            print(result)
exit