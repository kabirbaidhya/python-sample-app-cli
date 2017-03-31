user_list = []


def run():
    print()
    user = {}
    user['first_name'] = input('First Name: ')
    user['last_name'] = input('Last Lame: ')
    user['email'] = input('Email: ')
    user['address'] = input('Address: ')

    user_list.append(user)


def main():
    while True:
        # Run the program in the loop.
        run()
        print()
        
        # Ask the user if he wants more entries.
        should_continue = input('More Entries (Y/N)? ')

        # If the answer is not 'Y', exit.
        if should_continue.upper() != 'Y':
            break

    print(user_list)

main()
