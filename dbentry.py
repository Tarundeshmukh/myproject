import sqlite3
MySchool = sqlite3.connect("schooltest.db")

mysid = int(input("Enter studentID: "))
myname = input("Enter name: ")
myhouse = int(input("Enter house: "))
mymarks = float(input("Enter marks: "))

try:
	curschool = MySchool.cursor()
	curschool.execute("INSERT INTO students (StudentID, name, house, marks) VALUES (?, ?, ?, ?);", (mysid, myname, myhouse, mymarks))
	MySchool.commit()
	print("One record added successfully.")
except:
	print("Error in operation")
	MySchool.rollback()
MySchool.close()		
