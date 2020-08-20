from classes import ContactList

# Task 1.1
with open('contactlist.csv', 'r') as f:
    header = f.readline().strip().split(',')
    csvlist = []
    for line in f:
        name, email, mobile = line.strip().split(',')
        csvlist.append({'name': name,
                        'email': email,
                        'mobile': mobile,
                        })

# Task 1.3
contactlist = ContactList(100)
for contact in csvlist:
    contactlist.add(contact['name'], contact)

name = 'Joseff Stanley'
stored_contact = contactlist.get(name)
for email, mobile in (('wrongemail@gmail.com', '38468754'),
                      ('squadchattooga@gmail.com', '85744232'),
                      ):
    test = {'name': name, 'email': email, 'mobile': mobile}
    print(f'Testing "{name}" with email "{email}" and mobile "{mobile}":')
    print(f'stored details match test details: {test == stored_contact}')

print(contactlist.data)