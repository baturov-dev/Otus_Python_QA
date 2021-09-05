import csv
import json


def get_users(json_name):
    with open(json_name) as f:
        users = json.loads(f.read())
        users_list = [
             {
                 'name': user['name'],
                 'gender': user['gender'],
                 'address': user['address'],
                 'age': user['age'],
                 'books': []
             } for user in users
        ]
        return users_list


def get_books(csv_name):
    with open(csv_name) as f:
        reader = csv.DictReader(f)
        for entry in reader:
            book_dict = {
                'title': entry['Title'],
                'author': entry['Author'],
                'pages': entry['Pages'],
                'genre': entry['Genre']
            }
            yield book_dict


def distribute_books(users, books):
    i = 0
    users_count = len(users)
    for book in books:
        users[i]['books'].append(book)
        if i == users_count - 1:
            i = 0
        else:
            i += 1


def main():
    users = get_users('../files/users.json')
    books = get_books('../files/books.csv')
    distribute_books(users, books)

    with open('result.json', 'w') as f:
        json.dump( users, f)


if __name__ == '__main__':
    main()



