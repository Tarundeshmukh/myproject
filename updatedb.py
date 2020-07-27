import sqlite3
MySchool=sqlite3.connect('schooltest.db')
            
nm=input("enter name: ")
sql="SELECT * from students WHERE name='"+nm+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print (record)
"""m=float(input("enter new marks: "))
sql="UPDATE students SET marks='"+str(m)+"' WHERE name='"+nm+"';"
try:
    curschool.execute(sql)
    MySchool.commit()
    print ("record updated successfully")
except:
    print ("error in update operation")
    MySchool.rollback()"""

#deleting the retrieved record
res=input("Do you want to delete record? (Y/N) ")
sql="DELETE FROM students WHERE name='"+nm+"';"
if res=='Y':
     try:
       curschool.execute(sql)
       MySchool.commit()
       print ("record updated successfully")
     except:
        print ("error in update operation")
        MySchool.rollback()
MySchool.close()        
