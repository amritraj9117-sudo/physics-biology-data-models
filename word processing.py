# print('hello world')
def count_matches(d):
    count=0
    for k,v in d.items():
     if k==v:
        count+=1
    return count

def generate_word_dict(song):
    """Generates a frequency dictionary of words in a string."""
    b = song.lower()
    w = {}
    for word in b.split():
        if word in w:
            w[word] += 1
        else:
            w[word] = 1
    return w

def find_frequent_word(word_dict):
    """Finds the most frequent word(s) in a dictionary."""
    max_val = max(word_dict.values())
    w = [k for k, v in word_dict.items() if v == max_val]
    return (w, max_val)

def flatten(l):
    """Recursively flattens a nested list."""
    if not l:
        return []
    if isinstance(l[0], list):
        return flatten(l[0]) + flatten(l[1:])
    return [l[0]] + flatten(l[1:])

def address_book_app():
    """CLI application for address book."""
    def look_up(name):
        try:
            with open('addressbook.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    if name == lines[i].strip().lower():
                        return f"Entry found\nName={lines[i].strip()}\nAddress={lines[i+1].strip()}\nPhone={lines[i+2].strip()}"
        except FileNotFoundError:
            return 'Address book not found.'
        return None

    def add_entry(name, phone, address):
        with open('addressbook.txt', 'a') as file:
            file.write(f'{name}\n{address}\nPhone Number-{phone}\n')

    while True:
        print("\n1) Look up a person\n2) Add a person\n3) Quit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Name: ").strip().lower()
                print(look_up(name) or "Not found.")
            elif choice == 2:
                name = input("Name: ").strip().lower()
                phone = input("Phone (10 digits): ")
                addr = input("Address: ")
                add_entry(name, phone, addr)
                print("Added successfully.")
            elif choice == 3:
                break
        except ValueError:
            print("Invalid input.")

# --- Test Code ---
if __name__ == "__main__":
    song = 'RaH Rah AH AH rom mah RO mah MAH'
    word_dict = generate_word_dict(song)
    print(f"Word Dict: {word_dict}")
    print(f"Most Frequent: {find_frequent_word(word_dict)}")
    
    print(f"Flatten: {flatten([[1, 2], [3, 4], [9, 8, 7]])}")
    
    # Uncomment to run the address book app:
    # address_book_app()