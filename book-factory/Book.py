import random

class Book:
    def __init__(self, title, series, author):
        self.title = title
        self.series = series
        self.author = author

    def __repr__(self):
        return (
            f"Book(author='{self.author}', "
            f"title='{self.title}', series='{self.series}')"
        )

def generate_random_book() -> Book:
    authors = ["J.R.R Tolkien"]
    titles = ["The Two Towers"]
    series_list = ["The Lord of the Rings"]

    author = random.choice(authors)
    title = random.choice(titles)
    series = random.choice(series_list)

    return Book(author, title, series)

def main():
    book = generate_random_book()
    print("generated Book:")
    print(book)

if __name__ == "__main__":
    main()
