import sys
import os

sys.path.insert(0, os.getenv("HOME")+"/pyBookStore/class/")

from classStore import * 

database = os.getenv("HOME")+"/pyBookStore/database/books.db"

getFunc = BookStore()

if(os.path.isfile(database) == False):
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

