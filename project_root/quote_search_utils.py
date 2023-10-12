from models import Quote, Author
from mongoengine.queryset.visitor import Q

def search_quotes(author_name=None, tags=None):
    query = Quote.objects
    if author_name:
        author = Author.objects(fullname=author_name).first()
        if author:
            query = query.filter(author=author)
    if tags:
        query = query.filter(Q(tags__in=tags) | Q(tags=None))
    
    quotes = query
    return quotes

# Приклад використання для пошуку за автором та тегами:
author_name = "Albert Einstein"
tags = ["life", "live"]
quotes = search_quotes(author_name, tags)

for quote in quotes:
    print(f'Author: {quote.author.fullname}, Tags: {", ".join(quote.tags)}, Quote: {quote.quote}')