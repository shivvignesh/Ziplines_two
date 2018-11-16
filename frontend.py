from tkinter import *
from tkinter.ttk import *
from connector import *

LARGE_FONT=("Verdana",20)

class Ziplines(Tk):
	

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		Tk.configure(self)
		
		container=Frame(self)

		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		

		self.geometry("800x600")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (Home,Seller_info,Add_Products,Add_Employees,Add_Customers,display_products,display_employees,display_customers):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
			
		
		self.show_frame(Home)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()

class Home(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller


		label = Label(self, text="Home", font=LARGE_FONT )
		label.grid(row=2, column=2, padx=10,pady=10)
		
		
		button1=Button(self,text="Products",command=lambda:controller.show_frame(display_products))
		button2=Button(self,text="Employees",command=lambda:controller.show_frame(display_employees))
		# button3=Button(self,text="Add Products",command=lambda:controller.show_frame(Add_Products))
		button4=Button(self,text="Customers",command=lambda:controller.show_frame(Add_Customers))		
		button5=Button(self,text="display products",command=lambda:controller.show_frame(display_products))
		button6=Button(self,text="Seller info",command=lambda:controller.show_frame(Seller_info))


		button1.grid(row =4, column = 0, padx=20, pady =20)
		button2.grid(row = 4, column = 3, padx=20, pady =20)
		# button3.grid(row = 8,column =1,padx=20, pady =20 )
		button4.grid(row = 8,column =3,padx=20, pady =20 )
		button5.grid(row = 8,column =5,padx=20, pady =20 )
		button6.grid(row=8,column=7,padx=10,pady=10)

class Seller_info(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.seller_id_label = Label(self, text="seller id").grid(row=2,column=1,padx=10,pady=10)

		self.seller_name_label = Label(self, text="seller name").grid(row=3,column=1,padx=10,pady=10)

		self.seller_id=Text(self,height=2,width=30)
		self.seller_name=Text(self,height=2,width=30)
		
		self.seller_id.grid(row=2,column=2,padx=10,pady=10)
		self.seller_name.grid(row=3,column=2,padx=10,pady=10)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_seller)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)
	
	def add_seller(self):

		self.sid=self.seller_id.get("1.0","end-1c")
		self.sname=self.seller_name.get("1.0","end-1c")
		
		self.seller_id.delete("1.0","end")
		self.seller_name.delete("1.0","end")

		create_seller(self.sid,self.sname)

class Add_Products(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.product_id_label=Label(self,text="id of products")
		self.product_name_label=Label(self,text="Name of Product")
		self.product_price_label=Label(self,text="Price of Product")
		# self.seller_id_label=Label(self,text="id of seller")
		
		self.product_id=Text(self,height=2,width=30)
		self.product_name=Text(self,height=2,width=30)
		self.product_price=Text(self,height=2,width=30)
		# self.seller_id=Text(self,height=2,width=30)

		option=[]
		seller_ids=get_seller_id()

		for r in seller_ids:
			option.append(r)

		options = list(set(option))		#to obtain only unique events 
		variable = StringVar(self)
		variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, variable,*options,command=self.get_value).grid(row =6,column =1,padx=10,pady=10)
			

	
		self.product_id_label.grid(row=3,column=1,padx=10,pady=10)
		self.product_name_label.grid(row=4,column=1,padx=10,pady=10)
		self.product_price_label.grid(row=5,column=1,padx=10,pady=10)
		# self.seller_id_label.grid(row=6,column=1,padx=10,pady=10)

		self.product_id.grid(row=3,column=2,padx=10,pady=10)
		self.product_name.grid(row=4,column=2,padx=10,pady=10)
		self.product_price.grid(row=5,column=2,padx=10,pady=10)
		# self.seller_id.grid(row=6,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(display_products))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)

		self.submit_button=Button(self,text="Submit",command=self.add_product)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)


	def get_value(self,value):

		print(value)


		

	def add_product(self):
		self.pid=self.product_id.get("1.0","end-1c")
		self.pname=self.product_name.get("1.0","end-1c")
		self.pprice=self.product_price.get("1.0","end-1c")
		self.sid=self.seller_id.get("1.0","end-1c")

		self.product_id.delete("1.0","end")
		self.product_name.delete("1.0","end")
		self.product_price.delete("1.0","end")
		self.seller_id.delete("1.0","end")

		create_products(self.pid,self.pname,self.pprice,self.sid)

		display_products.add_to_tree(self.pid,self.pname,self.sid,self.pprice)

class Add_Employees(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.emp_id_label=Label(self,text="Id of Employee")
		self.emp_name_label=Label(self,text="Name of Employee")
		self.emp_gender_label=Label(self,text="Gender")
		self.emp_dob_label=Label(self,text="Employee Date of Birth")
		self.emp_salary_label=Label(self,text="Employee salary")
		self.emp_phno_label=Label(self,text="Phone Number")
		
		self.emp_id=Text(self,height=2,width=30)
		self.emp_name=Text(self,height=2,width=30)
		self.emp_gender=Text(self,height=2,width=30)
		self.emp_dob=Text(self,height=2,width=30)
		self.emp_salary=Text(self,height=2,width=30)
		self.emp_phno=Text(self,height=2,width=30)
		
		self.emp_id_label.grid(row=2,column=1,padx=10,pady=10)
		self.emp_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.emp_gender_label.grid(row=4,column=1,padx=10,pady=10)
		self.emp_dob_label.grid(row=5,column=1,padx=10,pady=10)
		self.emp_salary_label.grid(row=6,column=1,padx=10,pady=10)
		self.emp_phno_label.grid(row=7,column=1,padx=10,pady=10)

		self.emp_id.grid(row=2,column=2,padx=10,pady=10)
		self.emp_name.grid(row=3,column=2,padx=10,pady=10)
		self.emp_gender.grid(row=4,column=2,padx=10,pady=10)
		self.emp_dob.grid(row=5,column=2,padx=10,pady=10)
		self.emp_salary.grid(row=6,column=2,padx=10,pady=10)
		self.emp_phno.grid(row=7,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=2,column=5,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_employee)
		self.submit_button.grid(row=3,column=5,padx=20,pady=20)

	def add_employee(self):
			
			self.eid=self.emp_id.get("1.0","end-1c")
			self.ename=self.emp_name.get("1.0","end-1c")
			self.egender=self.emp_gender.get("1.0","end-1c")
			self.edob=self.emp_dob.get("1.0","end-1c")
			self.esalary=self.emp_salary.get("1.0","end-1c")
			self.ephno=self.emp_phno.get("1.0","end-1c")

			self.emp_id.delete("1.0","end")
			self.emp_name.delete("1.0","end")
			self.emp_gender.delete("1.0","end")
			self.emp_dob.delete("1.0","end")
			self.emp_salary.delete("1.0","end")
			self.emp_phno.delete("1.0","end")

			create_employees(self.eid, self.ename, self.egender, self.edob, self.esalary, self.ephno)


class Add_Customers(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.cust_id_label=Label(self,text="ID of customer")
		self.cust_name_label=Label(self,text="Name of customer")
		self.cust_phno_label=Label(self,text="Phone Number")
		self.cust_address_label=Label(self,text="Address")
		
		self.cust_id=Text(self,height=1,width=30)
		self.cust_name=Text(self,height=1,width=30)
		self.cust_phno=Text(self,height=1,width=30)
		self.cust_address=Text(self,height=10,width=30)
		
		self.cust_id_label.grid(row=2,column=1,padx=10,pady=10)
		self.cust_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.cust_phno_label.grid(row=4,column=1,padx=10,pady=10)
		self.cust_address_label.grid(row=5,column=1,padx=10,pady=10)

		self.cust_id.grid(row=2,column=2,padx=10,pady=10)
		self.cust_name.grid(row=3,column=2,padx=10,pady=10)
		self.cust_phno.grid(row=4,column=2,padx=10,pady=10)
		self.cust_address.grid(row=5,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=6,column=3,padx=20,pady=20) 		

		self.submit_button = Button(self,text="Submit",command=self.add_customer)
		self.submit_button.grid(row=6,column=2,padx=20,pady=20)

	def add_customer(self):

		self.cid = self.cust_id.get("1.0","end-1c")
		self.cname = self.cust_name.get("1.0","end-1c")
		self.cphno = self.cust_phno.get("1.0","end-1c")
		self.caddress = self.cust_address.get("1.0","end-1c")

		self.cust_id.delete("1.0","end")
		self.cust_name.delete("1.0","end")
		self.cust_phno.delete("1.0","end")
		self.cust_address.delete("1.0","end")

		create_customer(self.cid,self.cname,self.cphno,self.caddress)
class display_products(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Price')
		self.tree.heading('#4',text='seller id')

		self.tree.column('#1',stretch=YES)
		self.tree.column('#2',stretch=YES)
		self.tree.column('#3', stretch=YES)
		self.tree.column('#4', stretch=YES)
		self.tree.grid(row=4, column=4 ,padx=10,pady=10,columnspan=4, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree


		products=get_products()

		for i in products:
			self.tree.insert("",END,values=i)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=6,column=3,padx=20,pady=20) 		
		
		self.select_button=Button(self,text="delete",command=self.select_item)
		self.select_button.grid(row=6,column=4,padx=10,pady=10)

		self.add_product_button=Button(self,text="Add Products",command=lambda:controller.show_frame(Add_Products))
		self.add_product_button.grid(row=6,column=5,padx=10,pady=10)

	def select_item(self):
		 
		 self.curItem = self.tree.focus()
		 print (self.tree.item(self.curItem))
		 self.dict_item=self.tree.item(self.curItem)
		 print(type(self.dict_item))
		 self.product_list=[]
		 self.product_list=self.dict_item.get('values')
		 print(self.product_list)
		 self.product_id=self.product_list[0]
	

		 delete_product(self.product_id)

	def add_to_tree(pid,pname,sid,pprice):

		display_products.__init__(self,parent,controller).treeview.insert('', 'end', pid, pname, sid, pprice)
	 

class display_employees(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller


		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Gender')
		self.tree.heading('#4',text='dob')
		self.tree.heading('#5',text='salary')
		self.tree.heading('#6',text='Phone')

		self.tree.column('#1',stretch=YES)
		self.tree.column('#2',stretch=YES)
		self.tree.column('#3', stretch=YES)
		self.tree.column('#4', stretch=YES)
		self.tree.column('#5', stretch=YES)
		self.tree.column('#6', stretch=YES)

		self.tree.grid(row=4, column=4 ,padx=10,pady=10,columnspan=4, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		employees=get_employees()
		
		for i in employees:
			self.tree.insert("",END,values=i)

		self.back_button=Button(self,text="back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=6,column=3,padx=10,pady=10)

		self.select_button=Button(self,text="delete",command=self.delete_employee)
		self.select_button.grid(row=6,column=4,padx=10,pady=10)

		self.add_employee_button=Button(self,text="Add Employee",command=lambda:controller.show_frame(Add_Employees))
		self.add_employee_button.grid(row=6,column=5,padx=10,pady=10)

	def delete_employee(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.employee_list=[]
		self.employee_list=self.dict_item.get('values')
		print(self.employee_list)
		self.employee_id=self.employee_list[0]

		delete_employee(self.employee_id)
		

class display_customers(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Phone')
		self.tree.heading('#4',text='Address')

		self.tree.column('#1',stretch=YES)
		self.tree.column('#2',stretch=YES)
		self.tree.column('#3', stretch=YES)
		self.tree.column('#4', stretch=YES)


		self.tree.grid(row=4, column=4 ,padx=10,pady=10,columnspan=4, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		customers=get_customers()

		for i in customers:

			self.tree.insert("",END,values=i)

		self.back_button=Button(self,text="back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=6,column=3,padx=10,pady=10)
		

		self.add_customer_button=Button(self,text="Add customers",command=lambda:controller.show_frame(Add_Customers))
		self.add_customer_button.grid(row=6,column=5,padx=10,pady=10)
		
			

app=Ziplines()
app.mainloop()		