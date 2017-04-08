import store


def main():
    print('List of stored users:')
    users = store.load()

    print('First Name\t\tLast Name\tEmail\t\t\t\tAddress')

    # for each user in the user list
    for user in users:
        print('{}\t\t\t{}\t\t{}\t\t{}'.format(
            user['first_name'],
            user['last_name'],
            user['email'],
            user['address']
        ))

main()
