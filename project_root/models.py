from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    full_name = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, required=True)
    tags = ListField(StringField())
