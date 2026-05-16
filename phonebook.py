def look_up(name):
    """Looks up a name in address.txt and returns full 3 line records."""
    try:
        with open('addressbook.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                if name == lines[i].strip().lower():
                    name_found = lines[i].strip()
                    phone = lines[i+2].strip()
                    address = lines[i+1].strip()
                    return f"Entry found\nName={name_found}\nPhone={phone}\nAddress={address}"
    except FileNotFoundError:
        return 'Address book not found.'
    return None

def add_entry(name, phone, address):
    with open('addressbook.txt', 'a') as file:
        file.write(f'{name}\n')
        file.write(f'{address}\n')
        file.write(f'Phone Number-{phone}\n')

while True:
    print("\nWelcome")
    print("1) Look up a person by name")
    print("2) Add a person to the phonebook")
    print("3) Quit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Please enter the person's name: ").strip().lower()
            if not name.replace(" ", "").isalpha():
                raise ValueError("Name should contain only alphabets and spaces.")
            result = look_up(name)
            if result:
                print(result)
            else:
                print("Person not found in the phonebook.")
        elif choice == 2:
            name = input("Please enter the person's name: ").strip().lower()
            if not name.replace(" ", "").isalpha():
                raise ValueError("Name should contain only alphabets and spaces.")
            phone_number = input("Please enter phone number: ")
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Invalid phone number. Please provide a 10-digit number.")
            address = input("Please enter the address: ")
            add_entry(name, phone_number, address)
            print("Person added to the phonebook successfully.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Please provide a number less than or equal to 3.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        pass