import sqlite3
import os
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
		self.database=os.getenv("HOME")+"/pyBookStore/database/books.db"

	def openDB(self):
		self.conn = sqlite3.connect(self.database)
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
	
	def listByTittle(self,title):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE title = ?",(title))
		for row in self.c.fetchall():
			print(row)
		self.closeDB()

	def listByPrice(self,price):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books")
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def listByIsbn(self,isbn):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books")
		for row in self.c.fetchall():
			print(row)
		self.closeDB()

	def listByAuthor(self,author):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE author = ?",(author,))
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def listByCategory(self,category):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE category = ?",(category,))
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def listByPages(self,pages):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE pages = ?",(pages,))
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def listByFormat(self,Format):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE Format = ?",(Format,))
		for row in self.c.fetchall():
			print(row)
		self.closeDB()
	
	def listByRelease(self,pub_date):
		self.openDB()
		self.c.execute("SELECT rowid, * FROM books WHERE pub_date = ?",(pub_date))
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
		print("Enter:\n"
				"1 to add a new book,\n" 
				"2 to list all books,\n" 
				"3 to remove a book,\n" 
				"4 to search by keyword")
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
				if(len(isbn) == 6):
					self.checkIsbn(isbn)
					while(self.checkIsbn(isbn) != True):
						print("ISBN already exists")
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
			newbook = BookStore(title,author,price,isbn,category,
					Format,pages,pub_date)
			newbook.addNewBook()
		elif(option == 2):
			listStock = BookStore()
			listStock.printDB()
		elif(option == 3):
			print("Enter book's row that you want to delete :")
			rowNum = int(input())
			while(self.checkRow(rowNum) != True):
				print("Row : ",rowNum,"is empty")
				print("Try again:")
				rowNum = int(input())
			deletebook = BookStore()
			deletebook.delBook(rowNum)
		elif(option == 4):
			subprocess.call("clear",shell=True)
			listBy = BookStore()

			print("*" * 80)
			print("Enter:\n"
					"1 to search by Tittle,\n"
					"2 to search by author,\n"
					"3 to search by price,\n" 
					"4 to search by pages,\n"
					"5 to search by format,\n"
					"6 to search by release date\n")

			print("*" * 80)

			option = int(input())
			subprocess.call("clear",shell=True)


			if(option == 1):
				print("Enter title:")
				title = input()
				listBy.listByTittle(title)
			elif(option == 2):
				print("Enter author:")
				author = input().title()
				listBy.listByAuthor(author)
			elif(option == 3):
				print("Enter price:")
				price = float(input()) #MUST BE FIXED
				listBy.listByPrice(price)
			elif(option == 4):
				print("Enter pages:")
				pages = input()
				listBy.listByPages(pages)
			elif(option == 5):
				print("Enter format:")
				Format = input().title()
				listBy.listByFormat(Format)
			elif(option == 6):
				print("Enter release :") #MUST BE FIXED 
				release = input()
				listBy.listByRelease(release)




