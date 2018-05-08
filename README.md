# Distributed_Library

You have been hired by a library to build a distributed data storage system using a remote object paradigm that will allow their employees to access, store and update book information.

Each book has the following associated pieces of information which must be stored in the system:

1.	Book unique ID (this should be an integer value).
2.	Book author.
3.	Book ISBN (unique numeric commercial book identifier e.g. 9332549532).
4.	Book title.
5.	Book year of publication.
6.	Book status (currently on loan or not; this is a binary indicator).

Note, multiple copies of the same books will have the same ISBN but not the same unique ID.

Design and implement the above distributed data storage system using a remote object paradigm which allows employees to perform the following six tasks:

1.	Display all six pieces of information relating to the set of books currently stored.

2.	Add a book to the set of books currently stored; a newly added book should have a status of not on loan. The Book unique ID should be returned after completion of this task.

3.	Display the subset of books currently stored which have a publication date within a specified inclusive year range (e.g. 2000-2010).
4.	Display the subset of books currently stored which have a specified ISBN.
5.	Set the status of all books with a specified ISBN to on loan.
6.	Set the status of all books with a specified ISBN to not on loan.
 

Your system should determine which tasks to perform by parsing a CSV (comma separated values) file entitled tasks.txt sequentially where each line corresponds to an individual task.

A line corresponding to task 1 should have the following format d

A line corresponding to task 2 should have the following format a,author,ISBN,title,year

A line corresponding to task 3 should have the following format sy,year1,year2

Note, year1 equals the lower value of the range and year2 equals the upper value of the range.

A line corresponding to task 4 should have the following format si,ISBN

A line corresponding to task 5 should have the following format ol,ISBN

A line corresponding to task 6 should have the following format nol,ISBN

An example of a CSV file (tasks.txt) which the system should be able to parse is the
following:
d

a,James Munkres,9332549532,Topology,2015 a,Allen Hatcher,0521795400,Algebraic Topology,2001
a,Robert Ghrist,1502880857,Elementary Applied Topology,2014

sy,2000,2002
d
si,1502880857
ol,9332549532
nol,9332549532
