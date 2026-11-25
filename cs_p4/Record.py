class Book:
    #PUBLIC BookName: STRING
    #PUBLIC BookId : STRING
    #PUBLIC AuthorName : STRING
    def __init__(self, BookNameP, AuthorNameP, BookIdP ):
        self.BookName = BookNameP
        self.AuthorName = AuthorNameP
        self.BookId = BookIdP

Book1 = Book("Papersdock" , "MANAL" , "1234")
print(Book1.BookName)
Book2 = Book("Umairdheet", "Manal", "5678")
print(Book2.BookName)

class SaleData:
    #PUBLIC ProductId : STRING
    #PUBLIC ProductOty : INTEGER
    def __init__(self, ProductIdP , ProductQtyP):
        self.ProductId = ProductIdP
        self.ProductQty = ProductIdP

        
