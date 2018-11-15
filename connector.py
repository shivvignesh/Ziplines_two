import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='root',
	database='Ziplines'

	)

mycursor = mydb.cursor()

def create_seller(sid,sname):

	sql = "INSERT INTO seller (seller_id,seller_name) VALUES (%s, %s)"
	val=(sid,sname)
	mycursor.execute(sql, val)
	mydb.commit()

def get_seller():

	sql="SELECT * FROM seller"
	mycursor.execute(sql)

	sellers=mycursor.fetchall()
	return sellers

def create_products(pid,pname,pprice,sid):

	sql = "INSERT INTO products (product_id,product_name,seller_id,price) values (%s,%s,%s,%s) "
	val=(pid,pname,sid,pprice)
	mycursor.execute(sql,val)
	mydb.commit()

def create_employees(eid,ename,egender,edob,esalary,ephno):
	
	sql = "INSERT INTO employee (employee_id,employee_name,employee_gender,employee_dob,employee_salary,employee_phno) values (%s,%s,%s,%s,%s,%s)"
	val=(eid,ename,egender,edob,esalary,ephno)
	mycursor.execute(sql,val)
	mydb.commit()

def create_customer(cid, cname, cphno, caddress):

	sql = "INSERT INTO customer(customer_id, customer_name, customer_phno, customer_address) values (%s, %s, %s, %s)"
	val = (cid, cname, cphno, caddress)

	mycursor.execute(sql,val)
	mydb.commit() 		

def get_products():

	sql = "SELECT * FROM products"
	mycursor.execute(sql)
	products=mycursor.fetchall()

	return products

def delete_product(pid):

	sql = "DELETE FROM products WHERE product_id = %s"
	val=(pid,)

	mycursor.execute(sql,val)
	mydb.commit()

def get_employees():

	sql="SELECT * FROM employee"
	mycursor.execute(sql)
	employees=mycursor.fetchall()

	return employees

def delete_employee(eid):
	
	sql="DELETE FROM employee WHERE employee_id = %s "
	val=(eid,)
	
	mycursor.execute(sql,val)
	mydb.commit()	

def get_customers():

	sql="SELECT * FROM customer"
	mycursor.execute(sql)

	customers=mycursor.fetchall()
	return customers

def delete_customers(cid):

	sql= "DELETE FROM customer WHERE customer_id = %s"
	val=(cid,)

	mycursor.execute(sql,val)
	mydb.commit()