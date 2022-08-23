from email import message
from sqlite3 import adapt


name = "AdA lOvELacE"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name  = first_name + " " + last_name
message = ('Hello, ' + full_name.title() + '!')
print(message)