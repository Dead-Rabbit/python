import shelve
from classes.class_person import Person
shelvePath = "./db/class_shelve"
db = shelve.open(shelvePath)

bob = Person('bob', 10)
jack = Person('Jack',20)
db['bob'] = bob
db['Jack'] = jack
db.close()