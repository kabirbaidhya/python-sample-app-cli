# user_list = []
import store


def run():
    print()
    user = {}
    user['first_name'] = input('First Name: ')
    user['last_name'] = input('Last Lame: ')
    user['email'] = input('Email: ')
    user['address'] = input('Address: ')

    store.add(user)


def main():
    store.load()
    while True:
        # Run the program in the loop.
        run()
        print()

        # Ask the user if he wants more entries.
        should_continue = input('More Entries (Y/N)? ')

        # If the answer is not 'Y', exit.
        if should_continue.upper() != 'Y':
            break

    # This will save the user data to a file.
    store.save()

main()
