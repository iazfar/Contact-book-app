#empty dictionary
contacts = {}
while True:
    print('\nContact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter Your Choice = ')
  
    if choice == '1':
        name = input('Enter Your Name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter Age = ')
            email = input('Enter Email = ')
            mobile = input('Enter Mobile Number = ')          
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name}, Age:{age}, Email:{email}, Mobile Number:{mobile}')
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter name to update contact = ')
        if name in contacts:
            age = input('Enter Updated Age = ')
            email = input('Enter Updated Email = ')
            mobile = input('Enter Updated Mobile Number = ')  
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
        else:
            print('Contact not found!')

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact Name {name} has been deleted successfully!')
        else:
            print('Contact not found')

    elif choice == '5':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name:{name}, Age:{age}, Mobile Number:{mobile}, Email:{email}')
                found = True
        if not found:
            print('No contact found with that name')

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Closing the program...')
        break

    else:
        print('Invaild Input!')
