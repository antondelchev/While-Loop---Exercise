book_name = input()

command = ""
books_checked = 0

while command != "No More Books":
    if command == book_name:
        books_checked -= 1
        print(f"You checked {books_checked} books and found it.")
        break
    else:
        books_checked += 1
        command = input()

if command == "No More Books":
    books_checked -= 1
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
