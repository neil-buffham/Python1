with open("C:/Users/Tato Tower/Documents/Python1/Python1/Prepare activities/checkponts/w11/books.txt") as books_file:
    for line in books_file:
        book = line.strip()
        print(book)

    print()
    print("End of document")