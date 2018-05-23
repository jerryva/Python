
#!/usr/bin/env python

print '_-_-_-_-_-_-_-_-_-_-_-_-_- \n'

print 'press:1 for Create Table'
print 'press:2 for Insert Into '
print 'press:3 for Delete Table'
print 'press:4 for Modify Table'
print 'press:5 for Details'
print 'press:6 for exit'

print '_-_-_-_-_-_-_-_-_-_-_-_-_-'

import MySQLdb as My

eno= " "
ename=" "
esalary=" "
deptcode=" "

con = My.connect('Localhost','#username','#password','#connection')
cur = con.cursor()

choice=input("Enter a Choice :: ")

while choice!=7:
	if choice==1:	
		qs1="""
		create table bda_18_emp(eno int,ename char(30),esalary float,deptcode char(20),primary key(eno))"""

                qs2="""create table bda_18_dep(deptcode int,deptname char(30),deptaddrs char(50),primary key(deptcode)) """
		cur.execute(qs1)
		cur.execute(qs2)
		print "========================"
		print "Table is Created"
		choice=input("Enter new Choice :: ")

	if choice==2:
		print "========================"
		print "Enter the New Deatils"
		eno=raw_input('Enter the Eno. :: ')
		ename=raw_input('Enter the name :: ')
		esalary=raw_input('Enter the salary :: ')
		deptcode=raw_input('Enter the dept  :: ')
		qs1="insert into bda_18_emp values("+eno+",'"+ename+"',"+esalary+",'"+deptcode+"') "
		cur.execute(qs1)
		con.commit()
		con.rollback()
		print "------------------------"
		print "Values are Inserted"
		choice=input("Enter a new Choice :: ")
	if choice==3:
 		print "=========================="
		qs1= """ drop table bda_18_emp """
		cur.execute(qs1)
		print "=========================="
		print "Table is Deleted"
		print "=========================="
		choice=input("Enter New Choice :: ")
	if choice==4:
		print '=========================='
		print '      Updation Calls     '
		print '=========================='
		

		print 'press:1 For Eno. Updation'
		print 'press:2 For Name Updation'
		print 'press:3 For Salary Updation'
		print 'press:4 For Dept Upsation'
		print 'press:5 For Complete Updation \n'
		print '==============================='
		select=input("enter the updation choice")
		print '================================='
		while select!=5:
			if select==1:
				eno1=raw_input('enter the Eno. : ')
				qs1="update bda_18_emp set eno="+eno1+" where eno="+eno
                		cur.execute(qs1)
                		con.commit()
               			con.rollback()
				print '---------------------------'
				select=input("Enter 5 For Updation")
	
			if select==2:
                                ename1=raw_input('enter the Eno. : ')
                                qs1="update bda_18_emp set ename='"+ename1+"' where ename= '"+ename+"'"
                                cur.execute(qs1)
                                con.commit()
                                con.rollback()
				print '-----------------------------'
				select=input("Enter 5 For Updation ")
		  	if select==3:
                                esalary1=raw_input('enter the Salary : ')
                                qs1="update bda_18_emp set esalary="+esalary1+" where esalary= "+esalary
                                cur.execute(qs1)
                                con.commit()
                                con.rollback()
				print '---------------------------'
				select=input("Enter 5 For Updation ")

 	 		if select==4:
                                deptcode1=raw_input('enter the dept : ')
                                qs1="update bda_18_emp set deptcode='"+deptcode1+"' where deptcode='"+deptcode+"'"
                                cur.execute(qs1)
                                con.commit()
                                con.rollback()
				print '----------------------------'                    
               		        select=input("Enter 5 For Updation ")

		print '~~~~~~~~~~~~~~~~'
		print "Table is Updated"
		print '~~~~~~~~~~~~~~~~'
		choice=input("Enter New Choice :: ")

	if(choice==5):
		print "Enter table name"
		name=raw_input()
		a="select * from "+name	
		try:
			cur.execute(a)
		except Exception,arg:
			print "Error"
			print "Details : ",arg
		else:
			resc=cur.fetchall()
			print resc
			co.close()	
	if choice==6:
		print  '============='
		print  '\\\\\BYE/////'
		print  '============='
		break	
