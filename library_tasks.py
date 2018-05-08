import sys
import Pyro4
import Pyro4.util
import csv
import sys
import re

sys.excepthook = Pyro4.util.excepthook
warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")

#UNIQUE BOOK ID VARIABBLE
unique_id=1

# READ THE TXT FILE
f = open('./tasks.txt', 'r')
try:
	reader = csv.reader(f)
	for row in reader:

		# TASK 1 : DISPLAY ALL INFORMATION RELATING TO THE BOOKS CURRENTLY STORED 
		if row[0] == 'd':
			if not warehouse.list_contents():  
				print ("The Library Is Empty")
				print ('')
			else:
				print ("The Library Contains:")
				print (*warehouse.list_contents(),sep = "\n")
				print ('')

		# TASK 2 : STORE A BOOK SPECIFIED IN THE TXT FILE AND RETURN ITS UNIQUE ID
		elif row[0] == 'a':
			row[0] = unique_id
			row[2] = int(float(row[2]))
			row[4] = int(float(row[4]))
			row.append ("Not On Loan")
			unique_id += 1
			x=warehouse.store(row)
			print ("A Book Has Been Stored In The Library With Unique ID:",x)
			# print ('')

		# TASK 3 : DISPLAYS ALL BOOKS STORED IN THE LIBRARY WITH A SPECIFIC PUBLICATION DATE
		elif row[0] == 'sy':
			year1 = row[1]
			year2 = row[2]
			year1 = int(float(year1))
			year2 = int(float(year2))
			library = warehouse.list_contents()
			for book in library:
				for book_inforamtion in book:
					if isinstance(book_inforamtion, int):
						match = re.match(r'([1-3][0-9]{3})', str(book_inforamtion)) # REGEX IS USED TO DISTINQUISH YEAR FROM OTHER NUMERICAL VALUES IN BOOK_INFORMATION
						if match is not None:
							if book_inforamtion>=year1 and book_inforamtion<=year2:
								print ('')
								print ("The Books Published Between",year1,"And",year2,":")
								print (book)
								print ('')

		# TASK 4 : DISPLAY THE BOOK(S) WITH THE GIVEN ISBN
		elif row[0] == 'si':
			isbn = row[1]
			isbn = int(float(isbn))
			library = warehouse.list_contents()
			for book in library:
				
				for book_inforamtion in book:
					
					if isbn == book_inforamtion:
						print ('The Book With ISBN ',isbn,'Is:')
						print (book)
						print ('')

		# TASK 5 : SET THE STATUS OF ALL BOOKS WITH THE SPECIFIED ISBN TO 'ON LOAN'
		elif row[0] == 'ol':
			isbn = row[1]
			isbn = int(float(isbn))
			library = warehouse.list_contents()
			for book in library:
				for book_inforamtion in book:
					if isbn == book_inforamtion:
						if row[0] == 'ol':
							book[-1] = "On Loan"
			warehouse.clear()
			for book in library:
				warehouse.just_store(book)

		# # TASK 6 : SET THE STATUS OF ALL BOOKS WITH THE SPECIFIED ISBN TO 'NOT ON LOAN'
		elif row[0] == 'nol':
			isbn = row[1]
			isbn = int(float(isbn))
			library = warehouse.list_contents()
			for book in library:
				for book_inforamtion in book:
					if isbn == book_inforamtion:
						if row[0] == 'nol' :
							book[-1] = "Not On Loan"
			warehouse.clear()
			for book in library:
				warehouse.just_store(book)
		else:
			print ('*** WARNING ****  ------> {0} Is An Invalid Command, Check CSV File'.format (row[0]))

finally:
	f.close()