
book_list = {}

def create_book(title,author,year,pages):
    book_list["Title"] = title
    book_list["Author"] = author
    book_list["Year"] = year
    book_list["Pages"] = pages

create_book("Test Book","Benjamin", 2025,100)
create_book("Test Book 2","Sebastian", 2005,300)

print(book_list)


