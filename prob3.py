class LibraryBook:
    def __init__(self, book_id: int, title: str, author: str):
        self.b_i = book_id
        self.t = title
        self.a = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.t}' kitobi band qilindi.")

    def return_book(self):
        if not(self.is_available):
            self.is_available = True
            print(f"'{self.t}' kitobi qaytarildi.")

    def get_info(self):
        print(f"Kitob: {self.t} | Muallif: {self.a} | Holat: {self.is_available}")
        

kitob = LibraryBook(book_id=101, title="Sariq devni minib", author="Xudoyberdi To'xtaboyev")
kitob.borrow()
kitob.return_book()
kitob.get_info()