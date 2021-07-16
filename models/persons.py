from mongoengine import Document
from mongoengine import DateTimeField, StringField


class Person(Document):
    name = StringField(max_length=60, required=True)
    country = StringField(max_length=60)
    phone_number = StringField(max_length=20)
    birthday = DateTimeField()

    def __str__(self):
        return "{name:{}, country:{}, phone_number:{}, birthday:{}}".format(self.name, self.country, self.phone_number, self.birthday)
