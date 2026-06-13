class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def display_info(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f"'{self.title}' by {self.author} - {status}")

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"You have checked out {self.title}.")
        else:
            print(f"{self.title} is already checked out.")

# --- Using the class ---
book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

book1.display_info()
book1.check_out()
book1.display_info()    