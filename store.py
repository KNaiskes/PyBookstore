import sqlite3
import os.path
import subprocess

class BookStore:
	def __init__(self,title=None,author=None,price=None,isbn=None,
			category=None,Format=None,pages=None,pub_date=None):
		self.title = title 
		self.author = author
		self.price = price
		self.isbn = isbn
		self.category = category
		self.Format = Format
		self.pages = pages
		self.pub_date = pub_date 

	def openDB(self):
		self.conn = sqlite3.connect("books.db")
		self.conn.text_factory = str
		self.c = self.conn.cursor()
	def closeDB(self):
		self.closeC = self.c.close()
		self.save = self.conn.commit()
		self.close = self.c.close()

	   


	def checkIsbn(self,check):
		exists = None
		self.openDB()
		self.c.execute("SELECT * FROM books WHERE isbn = ?",(check,))
		count = self.c.fetchall()
		if (len(count) == 0):
			exists = True
		else:
			exists = False

		return exists
		self.closeDB()

	def addNewBook(self):
		self.openDB()
		self.c.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?,?,?,?)",
				(self.title,self.author,self.price,self.isbn,
					self.category,self.Format,self.pages,
					self.pub_date))
		self.closeDB()
	
	def propertiesTable(self):
		self.openDB()
		self.c.execute("""CREATE TABLE IF NOT EXISTS books(title TEXT,  
				author TEXT, price REAL,isbn TEXT, 
				category TEXT,Format TEXT,pages INTEGER, 
				pub_date TEXT)""")
		self.c.execute("INSERT INTO books VALUES(?,?,?,?,?,?,?,?) ",
				("Title","Author","Price","ISBN","Category",
					"Format","Pages","Publication Date"))
		self.closeDB()

	def printDB(self):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books")
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def checkRow(self,rowNumber):
		self.openDB()
		count = 0
		validRow = None

		self.c.execute("SELECT * FROM books")
		for row in self.c.fetchall():
			count += 1
		if(rowNumber > count):
			validRow = False
		else:
			validRow = True
		return validRow

	
	def delBook(self,rowNum):
		self.openDB()
		self.c.execute("DELETE FROM books WHERE rowid = ?",(rowNum,))
		self.c.execute("SELECT rowid, * FROM books")
		self.c.execute("VACUUM books")
		print("Done")
		self.closeDB()

	def menu(self):
		subprocess.call("clear",shell=True)
		print("*" * 80)
		print("Enter: 1 to add a new book, 2 to list all books, 3 to remove a book")
		print("*" * 80)
		option = int(input())
		if(option == 1):
			print("Enter book's title:")
			title = input().title()
			print("Enter book's author:")
			author = input().title()
			print("Enter price:")
			price = input()
			print("Enter book's ISBN code:")
			isbn = input()
			while(len(isbn) != 6):
				print("ISBN number must be a six digit number")
				print("Try again:")
				isbn = input()

			self.checkIsbn(isbn)
			while(self.checkIsbn(isbn) != True):
					print("There is already a book with isbn ",isbn)
					print("Try again:")
					isbn = input()
			print("Enter book's category:")
			category = input().title()
			print("Enter book's format:")
			Format = input().title()
			print("Enter book's pages:")
			pages = input()
			print("Enter publication date of the book:")
			pub_date = input()
			newbook = BookStore(title,author,price,isbn,category,Format,pages,pub_date)
			newbook.addNewBook()
		elif(option == 2):
			listStock = BookStore()
			listStock.printDB()
		elif(option == 3):
			print("Enter book's row number that you want to delete :")
			rowNum = int(input())
			while(self.checkRow(rowNum) != True):
				print("Row : ",rowNum,"is empty")
				print("Try again:")
				rowNum = int(input())
			deletebook = BookStore()
			deletebook.delBook(rowNum)

getFunc = BookStore()

if(os.path.isfile("books.db") == False):
	getFunc.propertiesTable()

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

