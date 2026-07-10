class Book:
    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"ID: {self.book_id} | {self.title} by {self.author} | {status}"


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) | Books borrowed: {len(self.borrowed_books)}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}
        self.transactions = []

    def add_book(self, book):
        """Add a new book to the library"""
        if book.book_id in self.books:
            print(f"Book with ID {book.book_id} already exists!")
            return False
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully!")
        return True

    def remove_book(self, book_id):
        """Remove a book from the library"""
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_available:
                print(f"Cannot remove '{book.title}' - it is currently borrowed!")
                return False
            del self.books[book_id]
            print(f"Book '{book.title}' removed successfully!")
            return True
        print(f"Book with ID {book_id} not found!")
        return False

    def register_member(self, member):
        """Register a new member"""
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists!")
            return False
        self.members[member.member_id] = member
        print(f"Member '{member.name}' registered successfully!")
        return True

    def borrow_book(self, book_id, member_id):
        """Borrow a book"""
        if book_id not in self.books:
            print(f"Book with ID {book_id} not found!")
            return False

        if member_id not in self.members:
            print(f"Member with ID {member_id} not found!")
            return False

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.is_available:
            print(f"Sorry, '{book.title}' is currently not available!")
            return False

        if len(member.borrowed_books) >= 3:
            print(f"Member '{member.name}' has reached the maximum borrowing limit (3 books)!")
            return False

        # Borrow the book
        book.is_available = False
        book.borrowed_by = member.name
        member.borrowed_books.append(book.book_id)
        self.transactions.append({
            'type': 'BORROW',
            'book_id': book_id,
            'member_id': member_id,
            'book_title': book.title,
            'member_name': member.name
        })
        print(f"'{book.title}' borrowed successfully by {member.name}!")
        return True

    def return_book(self, book_id, member_id):
        """Return a borrowed book"""
        if book_id not in self.books:
            print(f"Book with ID {book_id} not found!")
            return False

        if member_id not in self.members:
            print(f"Member with ID {member_id} not found!")
            return False

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_available:
            print(f"'{book.title}' is already available in the library!")
            return False

        if book_id not in member.borrowed_books:
            print(f"Member '{member.name}' did not borrow this book!")
            return False

        # Return the book
        book.is_available = True
        book.borrowed_by = None
        member.borrowed_books.remove(book_id)
        self.transactions.append({
            'type': 'RETURN',
            'book_id': book_id,
            'member_id': member_id,
            'book_title': book.title,
            'member_name': member.name
        })
        print(f"'{book.title}' returned successfully by {member.name}!")
        return True

    def search_books(self, search_term):
        """Search books by title or author"""
        found = []
        search_term = search_term.lower()
        for book in self.books.values():
            if search_term in book.title.lower() or search_term in book.author.lower():
                found.append(book)
        
        if found:
            print(f"\nFound {len(found)} book(s):")
            for book in found:
                print(f"  {book}")
        else:
            print("No books found matching your search!")
        return found

    def display_books(self):
        """Display all books in the library"""
        if not self.books:
            print("No books in the library!")
            return
        
        print(f"\n{'='*50}")
        print(f"LIBRARY: {self.name}")
        print(f"{'='*50}")
        print(f"Total Books: {len(self.books)}")
        print(f"Available: {sum(1 for b in self.books.values() if b.is_available)}")
        print(f"Borrowed: {sum(1 for b in self.books.values() if not b.is_available)}")
        print(f"{'='*50}")
        for book in self.books.values():
            print(f"  {book}")

    def display_members(self):
        """Display all registered members"""
        if not self.members:
            print("No members registered!")
            return
        
        print(f"\n{'='*50}")
        print("REGISTERED MEMBERS")
        print(f"{'='*50}")
        for member in self.members.values():
            borrowed_titles = [self.books[id].title for id in member.borrowed_books if id in self.books]
            print(f"  {member}")
            if borrowed_titles:
                print(f"    Currently reading: {', '.join(borrowed_titles)}")

    def display_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("No transactions yet!")
            return
        
        print(f"\n{'='*50}")
        print("TRANSACTION HISTORY")
        print(f"{'='*50}")
        for i, trans in enumerate(self.transactions, 1):
            print(f"  {i}. {trans['type']} - '{trans['book_title']}' by {trans['member_name']}")


# Main program with menu
def main():
    # Create a library
    library = Library("City Central Library")

    # Add some sample books
    library.add_book(Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5"))
    library.add_book(Book(2, "1984", "George Orwell", "978-0-4522-8423-4"))
    library.add_book(Book(3, "To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"))
    library.add_book(Book(4, "The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0"))
    library.add_book(Book(5, "Dune", "Frank Herbert", "978-0-441-17271-9"))

    # Register some members
    library.register_member(Member(101, "Alice Johnson", "alice@email.com"))
    library.register_member(Member(102, "Bob Smith", "bob@email.com"))
    library.register_member(Member(103, "Carol White", "carol@email.com"))

    while True:
        print("\n" + "="*50)
        print("📚 LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Display All Books")
        print("2. Search Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View Members")
        print("6. View Transactions")
        print("7. Add New Book")
        print("8. Remove Book")
        print("9. Register New Member")
        print("0. Exit")
        print("="*50)
        
        try:
            choice = input("Enter your choice (0-9): ")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        if choice == '0':
            print("Thank you for using the Library Management System. Goodbye! 👋")
            break

        elif choice == '1':
            library.display_books()

        elif choice == '2':
            search = input("Enter title or author to search: ")
            library.search_books(search)

        elif choice == '3':
            try:
                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Member ID: "))
                library.borrow_book(book_id, member_id)
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == '4':
            try:
                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Member ID: "))
                library.return_book(book_id, member_id)
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == '5':
            library.display_members()

        elif choice == '6':
            library.display_transactions()

        elif choice == '7':
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                isbn = input("Enter ISBN: ")
                library.add_book(Book(book_id, title, author, isbn))
            except ValueError:
                print("Invalid input!")

        elif choice == '8':
            try:
                book_id = int(input("Enter Book ID to remove: "))
                library.remove_book(book_id)
            except ValueError:
                print("Invalid input!")

        elif choice == '9':
            try:
                member_id = int(input("Enter Member ID: "))
                name = input("Enter Member Name: ")
                email = input("Enter Email: ")
                library.register_member(Member(member_id, name, email))
            except ValueError:
                print("Invalid input!")

        else:
            print("Invalid choice! Please enter a number between 0-9.")


if __name__ == "__main__":
    main()