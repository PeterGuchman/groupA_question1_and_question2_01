import mysql. connector as a
#In the password sector in the connect function place your database's password and it leave empty in case you didn't set one
con=a.connect (host=" localhost", user=" root", password="m", database="Library")
#Returns 'True' if there is a connection
print(con.is_connected())
c=con.cursor()

def addmember():
 bn=input("enter the member name : ")
 c=input ( "enter the member regno : ")
 data=(bn,c)
 sql='insert into members values(%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("MEMBER ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def updatememb():
 ac=input("enter  member regno:")
 bc=input("enter member name:")
 a="UPDATE members SET NAME=%s WHERE REGNO=%s"
 data=(bc,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print (c.rowcount)
 print("MEMBER UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def deletememb():
 c=input ( "enter the member regno : ")
 data=(c,)
 sql="delete from members where regno=%s"
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("MEMBER DELETED SUCCESSFULLY")
 main()

def dispmemb():
 a="select * from members"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No members available....ADD MEMBER")
 else:
     print("Members available:")
 for i in myresult:
     print("Member name : ",i[0])
     print("Member regno : ",i[1])
     print ("============= ")




def addpub():
 bn=input("enter the publication name : ")
 c=input ( "enter the publication code : ")
 t=input( "total book : ")
 s=input("enter subject : ")
 data=(bn,c, t, s)
 sql='insert into books values(%s,%s,%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("BOOK ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def searchpub():
 bn=input("enter the publication name : ")
 c=input ( "enter the publication code : ")
 data=(bn,c)
 a="slect * from books where BCODE=%s AND BNAME=%s"
 vals = (options_var.get(), search_text_var.get())
 c=con.cursor()
 c.execute(a,data,vals)
 my_rows = c.fetchall()
 print(my_rows)
 print ("=============")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def issued():
 n=input ( "enter loaner name : ")
 r=input("enter the reg no:")
 co=input ( "enter book code:")
 d=input("enter date : ")
 a='insert into issue values(%s,%s,%s,%s)'
 data=(n,r,co,d)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("Book Issued To :",n)
 bookup(co, -1)
 main()

def dispissue():
 a="select * from issue"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No issue available....ADD ISSUE")
 else:
     print("Issue available:")
 for i in myresult:
     print(" name : ",i[0])
     print("regno : ",i[1])
     print("bcode : ",i[2])
     print("issue date:",i[3])
     print ("============= ")

def returnp():
 n=input ( "enter the name : ")
 r=input ( "enter the reg no:")
 co=input("enter book code : ")
 d=input ( "enter date : ")
 a=' insert into submit values(%s,%s,%s,%s)'
 data=(n,r,co,d)
 c=con. cursor()
 c. execute ( a, data)
 con.commit()

 a="delete from issue where regno=%s"
 data=(r,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()

 
 print ("=============")
 print (" Book returned by :",n)
 bookup(co,+1)
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def bookup(co,u):
 a="select TOTAL from books where BCODE = %s"
 data=(co,)
 c=con. cursor()
 c.execute(a,data)
 myresult=c. fetchone ()
 t=myresult[0] + u
 sql="update books set TOTAL = %s where BCODE =%s"
 d=(t,co)
 c. execute ( sql,d)
 con.commit()
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def updatepub():
 ac=input("enter  book  code:")
 bc=input("enter book name:")
 a="UPDATE books SET BNAME=%s WHERE BCODE=%s"
 data=(bc,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print (c.rowcount)
 print("PUBLICATION UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def deletepub():
 ac=input("enter  book  code:")
 a="delete from books where BCODE=%s"
 data=(ac,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("BOOK DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def dispbook():
 a="select * from books"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No books available...ADD A BOOK ")
 else:
     print("Books available:")
 for i in myresult:
     print("book name : ",i[0])
     print("book code : ",i[1])
     print("total : ",i[2])
     print("subject:",i[3])
     print ("============= ")


def dsubmit():
 ad=input("enter name:")
 a="delete from submit where name=%s"
 data=(ad,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("SUBMISSION DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 main()

def main():    
 print("""

WELCOME TO THE LIBRARY MANAGEMNT SYSTEM

1.ADD PUBLICATION
2.UPDATE PUBLICATION
3.ISSUE PUBLICATION
4.RETURN PUBLICATION
5.DELETE PUBLICATION
6.DISPLAY PUBLICATION
7.ADD MEMBER
8.DELETE MEMBER
9.SEARCH PUBLICATION
10.UPDATE MEMBER
11.DISPLAY MEMBERS
12.DISPLAY ISSUE""")
main()

while True:
    try:
        choice=int(input("Enter  Task No:"))
        if (choice==1):
            addpub()
            break
        elif(choice==2):
            updatepub()
            break
        elif(choice==3):
            issued()
            break
        elif(choice==4):
            returnp()
            break
        elif(choice==5):
            deletepub()
            break
        elif(choice==6):
            dispbook()
            break
        elif(choice==7):
            addmember()
            break
        elif(choice==8):
            deletememb()
            break
        elif(choice==9):
            searchpub()
            break
        elif(choice==10):
            updatememb()
            break
        elif(choice==11):
            dispmemb()
            break
        elif(choice==12):
            dispissue()
            break
        else:
            print("Invalid choice.Enter 1-5...")
            main()
           
    except ValueError:
            print("Invalid choice.Enter 1-5")
            exit
            main()
           


        
   
        
            
    
