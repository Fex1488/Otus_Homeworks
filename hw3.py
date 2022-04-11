import csv
import json

try:
    with open('books.csv', 'r') as file1:
        books = []
        for i_book in list(csv.DictReader(file1)):
            books.append(
                {'title': i_book.get('Title'),
                 'author': i_book.get('Author'),
                 'pages': i_book.get('Pages'),
                 'genre': i_book.get('Genre')}
            )
except FileNotFoundError:
    print('books файла нет')

try:
    with open('users.json', 'r') as file2:
        users = []
        for i_user in json.load(file2):
            users.append(
                {'name': i_user.get('name'),
                 'gender': i_user.get('gender'),
                 'address': i_user.get('address'),
                 'age': i_user.get('age'),
                 'books': []})
except FileNotFoundError:
    print('users файла нет')

while len(books) > 0:
    for i_user in users:
        if len(books) > 0:
            i_user['books'].append(books.pop())

with open('result.json', 'w') as file3:
    json.dump(users, file3, indent=4)


