from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)



class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()


db.connect()


db.drop_tables([Contact])
db.create_tables([Contact])

Michael = Contact(first_name='Michael', last_name='Scott', phone='5704565590')
Michael.save()
Dwight = Contact(first_name='Dwight', last_name='Schrute', phone='5700440670')
Dwight.save()
Jim = Contact(first_name='Jim', last_name='Halpert', phone='5700103489')
Jim.save()
Pam = Contact(first_name='Pam', last_name='Beesly', phone='5700140003')
Pam.save()
Creed = Contact(first_name='Creed', last_name='Bratton', phone='5706778880')
Creed.save()
Angela = Contact(first_name='Angela', last_name='Martin', phone='5703217878')
Angela.save()
Kevin = Contact(first_name='Kevin', last_name='Malone', phone='5703425768')
Kevin.save()
Andy = Contact(first_name='Andy', last_name='Bernard', phone='5701113425')
Andy.save()
Toby = Contact(first_name='Toby', last_name='Flenderson', phone='5705435468')
Toby.save()
Stanley = Contact(first_name='Stanley', last_name='Hudson', phone='5701234259')
Stanley.save()
Kelly = Contact(first_name='Kelly', last_name='Kapoor', phone='5706574900')
Kelly.save()
Ryan = Contact(first_name='Ryan', last_name='Howard', phone='5701124368')
Ryan.save()
Oscar = Contact(first_name='Oscar', last_name='Martinez', phone='5706758890')
Oscar.save()
Darryl = Contact(first_name='Darryl', last_name='Philbin', phone='5701324454')
Darryl.save()
Meredith = Contact(first_name='Meredith', last_name='Palmer', phone='5701324335')
Meredith.save()



def start():
    print()
    print("**********   Contact Book Main Menu   **********\n")
    print("Please choose a number from the following option below:")
    print(" 1. Get all contacts")
    print(" 2. Search single Contact")
    print(" 3. Create new contact")
    print(" 4. Exit")
    pick = int(input())
    return pick

def main():
    entry = start()
    while entry != 4:
        if entry == 1:
            for info in Contact.select():
                print(f"{contact.first_name}, {contact.last_name}, {contact.phone}")
        elif entry == 2:
            # search single contact
        elif entry == 3:
            # create contact
        else 
            print("invalid entry")
        entry = menu()


    

main()