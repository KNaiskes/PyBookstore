import sqlite3

class BookStore:
	def __init__(self,title=None,author=None,price=None,isbn=None):
		self.title = title 
		self.author = author
		self.price = price
		self.isbn = isbn
		
	def checkIsbn(self,check):
		exists = None
		conn = sqlite3.connect("books.db")
		conn.text_factory = str
		c = conn.cursor()
		c.execute("SELECT * FROM books WHERE isbn = ?",(check,))
		count = c.fetchall()
		if (len(count) == 0):
			exists = True
		else:
			exists = False

		return exists

		conn.commit()
		c.close()
		conn.close()

	def addNewBook(self):
		conn = sqlite3.connect('books.db')
		conn.text_factory = str
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT, price REAL,isbn TEXT)")
		c.execute("INSERT INTO books VALUES(?, ?, ?, ?)",(self.title,self.author,self.price,self.isbn))
		conn.commit()
		c.close()
		conn.close()

	def printDB(self):
		conn = sqlite3.connect("books.db")
		conn.text_factory = str
		c  = conn.cursor()
		c.execute("SELECT * FROM books")
		for row in c.fetchall():
			print(row)
		conn.commit()
		c.close()
		conn.close()
	
	def delBook(self,delisbn):
		conn = sqlite3.connect("books.db")
		conn.text_factory = str
		c = conn.cursor()
		c.execute("SELECT * FROM books WHERE isbn = ?",(delisbn,))
		count  = c.fetchall()
		if (len(count) == 0):
			print("There is no book with isbn :",delisbn)
		else:
			c.execute("DELETE FROM books WHERE isbn=?",(delisbn,))
		conn.commit()
		c.close()
		conn.close()

	def menu(self):
		print("*************************************************************************")
		print("Enter: 1 to add a new book, 2 to list all books, 3 to remove a book")
		print("*************************************************************************")
		option = int(input())
		if(option == 1):
			print("Enter book's title:")
			title = input()
			print("Enter book's author:")
			author = input()
			print("Enter price:")
			price = input()
			print("Enter book's ISBN code:")
			isbn = input()
			while(self.checkIsbn(isbn) != True):
					print("There is already a book with isbn ",isbn)
					print("Try again:")
					isbn = input()
			self.checkIsbn(isbn)
			newbook = BookStore(title,author,price,isbn)
			newbook.addNewBook()
		elif(option == 2):
			listStock = BookStore()
			listStock.printDB()
		elif(option == 3):
			print("Enter book's ISBN code that you want to delete:")
			deleteIsbn = input()
			deletebook = BookStore()
			deletebook.delBook(deleteIsbn)

getFunc = BookStore()

getFunc.menu()

while(True):
	print()
	print()
	print("Do you want to do more actions ? y/n :")
	answ = input()
	if(answ == "y"):
		getFunc.menu()
	elif(answ == "n"):
		print("GoodBye!")
		break
	else:
		print("Unknown command. Try again")

