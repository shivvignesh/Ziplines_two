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

def get_seller_id():

	sql="SELECT seller_id from seller"
	mycursor.execute(sql)

	seller_ids=mycursor.fetchall()
	return seller_ids

def create_orders(oid, pid, pname, sid, sname, pprice, cid, cname, stat, ename):

	sql = "INSERT INTO orders(order_id, product_id, product_name, seller_id, seller_name, price, customer_id, customer_name, status, employee_name) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (oid, pid, pname, sid, sname, pprice, cid, cname, stat, ename)

	mycursor.execute(sql,val)
	mydb.commit()

def get_orders():

	sql="SELECT * FROM orders"
	mycursor.execute(sql)

	orders=mycursor.fetchall()
	return orders

def delete_order(oid):

	sql= "DELETE FROM orders WHERE order_id = %s"
	val=(oid,)

	mycursor.execute(sql,val)
	mydb.commit()	

def get_product_id():

	sql="SELECT product_id from products"
	mycursor.execute(sql)

	product_ids=mycursor.fetchall()
	return product_ids

def get_customer_id():

	sql="SELECT customer_id from customer"
	mycursor.execute(sql)

	customer_ids=mycursor.fetchall()
	return customer_ids

def get_customer_name(cid):

	sql="SELECT customer_name from customer WHERE customer_id = %s"
	val=(cid,)
	mycursor.execute(sql,val)

	customer_names=mycursor.fetchall()
	return customer_names

def get_product_name(pid):

	sql="SELECT product_name from products WHERE product_id = %s"
	val=(pid,)
	mycursor.execute(sql,val)

	product_names=mycursor.fetchall()
	return product_names

def get_seller_name(sid):

	sql="SELECT seller_name from seller WHERE seller_id = %s"
	val=(sid,)
	mycursor.execute(sql,val)

	seller_names=mycursor.fetchall()
	return seller_names

def get_seller_id():

	sql="SELECT seller_id from seller"
	mycursor.execute(sql)

	seller_ids=mycursor.fetchall()
	return seller_ids

def get_seller_name():

	sql="SELECT products.product_id, products.product_name, seller.seller_id, seller.seller_name from products INNER JOIN seller WHERE products.seller_id = seller.seller_id"
	mycursor.execute(sql)

	seller_name=mycursor.fetchall()
	return seller_name

def search_products(pname,pprice):

	sql="SELECT * from products WHERE product_name=%s and price<=%s"
	val=(pname,pprice)

	mycursor.execute(sql,val)
	products=mycursor.fetchall()
	return products

def update_product(pid,pname,pprice,sid):

	sql="UPDATE products set product_name=%s,price=%s,seller_id=%s WHERE product_id=%s"
	val=(pname,pprice,sid,pid)

	mycursor.execute(sql,val)
	mydb.commit()

	sql="SELECT * FROM products WHERE product_id=%s"
	val=(pid,)
	mycursor.execute(sql,val)
	new_product=mycursor.fetchall()
	return new_product

def update_employee(eid,ename,egender,edob,esalary,ephno):

	sql="UPDATE employee set employee_name=%s,employee_gender=%s,employee_dob=%s,employee_salary=%s,employee_phno=%s WHERE employee_id=%s"
	val=(ename,egender,edob,esalary,ephno,eid)

	mycursor.execute(sql,val)
	mydb.commit()

def update_customer(cid,cname,cphno,caddress):

	sql="UPDATE customer set customer_name=%s,customer_phno=%s,customer_address=%s WHERE customer_id=%s"
	val=(cname,cphno,caddress,cid)

	mycursor.execute(sql,val)
	mydb.commit()





