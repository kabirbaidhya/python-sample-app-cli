import store


def main():
    users = store.load()
    print_users(users)


def print_users(users):
    print('List of stored users:')
    print('First Name\t\tLast Name\tEmail\t\t\t\tAddress')
    print('-' * 80)
    # for each user in the user list
    for user in users:
        print('{}\t\t\t{}\t\t{}\t\t{}'.format(
            user['first_name'],
            user['last_name'],
            user['email'],
            user['address']
        ))
    print('-' * 80)

main()
