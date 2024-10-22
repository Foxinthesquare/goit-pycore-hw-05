def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments provided."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Not enough arguments.")
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    if len(args) < 1:
        raise ValueError("Not enough arguments.")
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def get_all_contacts(args, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command in ['exit', 'close', 'goodbye']:
            print("Goodbye!")
            break

        args = input("Enter the argument for the command: ").strip().split()

        if command == 'add':
            response = add_contact(args, contacts)
        elif command == 'phone':
            response = get_phone(args, contacts)
        elif command == 'all':
            response = get_all_contacts(args, contacts)
        else:
            response = "Unknown command. Please use 'add', 'phone', or 'all'."

        print(response)
