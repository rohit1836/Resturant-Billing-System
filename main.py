from tkinter import *
import random
import datetime
from tkinter.ttk import Combobox
from tkinter import messagebox as tmsg
import mysql.connector as msc
import tkinter.filedialog as fd

root = Tk()

window_width = 1400
window_height = 800
root.geometry(f"{window_width}x{window_height}")
root.minsize(1400,800)
root.title("Restaurant Bill Management System")


# ===========================================Main Billing Window ================================================

def billManagementWindow():
    

    bill_management_window = Toplevel()
    bill_management_window.title("Restaurant Billing System")

    # Header of the Main Window
    header_frame = Frame(bill_management_window,padx=10,pady=10,bg="orange",border=5,relief=GROOVE)
    header_frame.pack(side=TOP,anchor=N,fill=X)

    header_label = Label(header_frame,text="Restaurant Billing System",bg="yellow",fg="black",width=3,height=3,font="obelixpro 30")
    header_label.pack(fill=X)

    # ========================================Body of the Main Window========================================
    main_frame = Frame(bill_management_window,padx=5,pady=10)
    main_frame.pack(ipadx=5,ipady=10)

    # Details Area
    details_frame = Frame(main_frame,padx=0,pady=0,border=10,relief=GROOVE)
    details_frame.pack(side=LEFT,anchor=W,fill=Y,ipadx=5,ipady=5)

    Label(details_frame,text="Enter Details Here",font="mouser 20",border=7,relief=RAISED,padx=5,pady=5).grid(row=0,column=0,columnspan=3,sticky=N+E+W+S,padx=5,pady=5)
    Label(details_frame,text="").grid(row=1,column=0)
    Label(details_frame,text="").grid(row=1,column=1)

    Label(details_frame,text="Bill No. : ",font="cambria 18").grid(row=2,column=0,sticky=N+E+W+S)
    Label(details_frame,text="Customer Name : ",font="cambria 18").grid(row=3,column=0)
    Label(details_frame,text="Customer Contact : ",font="cambria 18").grid(row=4,column=0)
    Label(details_frame,text="Date : ",font="cambria 18").grid(row=5,column=0)
    Label(details_frame,text="Item : ",font="cambria 18").grid(row=6,column=0)
    Label(details_frame,text="Quantity : ",font="cambria 18").grid(row=7,column=0)
    Label(details_frame,text="per cost : ",font="cambria 18").grid(row=8,column=0)


    # Bill number
    global bill_no
    bill_no = StringVar(value=str(random.randint(0,1000)))
    Entry(details_frame,font="cambria 18",textvariable=bill_no,state=DISABLED).grid(row=2,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)

    # Customer Name
    global customer_name 
    customer_name = StringVar()
    customer_name_entry_box = Entry(details_frame,font="cambria 18",textvariable=customer_name)
    customer_name_entry_box.grid(row=3,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)

    # Customer Contact
    global customer_contact 
    customer_contact = StringVar()
    customer_contact_entry_box = Entry(details_frame,font="cambria 18",textvariable=customer_contact)
    customer_contact_entry_box.grid(row=4,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)

    # Date
    global date
    date = StringVar()
    date.set(datetime.date.today())
    date_label = Entry(details_frame,font="cambria 18",textvariable=date,state=DISABLED)
    date_label.grid(row=5,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)

    # Food Menu 
    global food_menu
    food_menu = {"Normal thali" : 60,
"Special Thali" : 80,
"Aaloo Parantha" : 50,
"Gobhi Parantha": 50,
"Rajma" : 60,
"Shahi Paneer" : 100,
"Mutter Paneer" : 80,
"Cholley" : 60,
"Jeera Rice" : 40,
"Roti" : 5,
"Parantha" : 15,
"Veg. Manchurian" : 100,
"Veg. Soup" : 40,
"Veg. Fried Rice" : 70,
"Veg. Chowmein" : 80,
"Paneer Chowmien" : 80,
"Momos" : 50,
"Normal Maggi" : 30,
"Masala Maggi" : 35,
"Boil Egg Maggi" : 40,
"Butter Maggi" :50,
"Paneer Maggi" : 55,
"Cheese Maggi" : 60,
"Red Pasta" : 45,
"White Pasta" : 55,
"Pasta With Cheese" : 100,
"Veg. Macroni" : 80,
"Cheese Macroni" : 100,
"Veg. Sandwich" : 25,
"Sandwich Tomato Cheese" : 60,
"Grilled Veg. Sandwich" : 35,
"Cheese Sandwich" : 60,
"Veg. Burger" : 40,
"Tikki Burger" : 50,
"Egg Burger" : 55,
"Cheese Burger" : 60,
"Tea" : 15,
"Coffee" : 20,
"Buttermilk" : 15,
"Pineapple Buttermilk" : 20,
"Nimbu Paani" : 20,
"Nimbu Soda" : 25,
"Pineapple Jal Jeera" : 25,
"Rose Lemonade" : 25,
"Mango Shake" : 30,
"Pineapple Shake" : 30,
"Vanilla Shake" : 30,
"Chocolate Shake" : 35,
"Oreo Vanilla Shake" : 40,
"Oreo Chocolate Shake" : 45
}

    # Items 
    food_menu_items_list = []
    for items in food_menu.keys():
        food_menu_items_list.append(items)
    global item_value 
    item_value = StringVar()
    item_dropdown = Combobox(details_frame,textvariable=item_value,font="cambria 15",state=DISABLED)
    item_dropdown.grid(row=6,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)
    item_dropdown['values'] = food_menu_items_list
    item_dropdown.current(0)
    item_dropdown.bind("<<ComboboxSelected>>",updatePerCostValue)

    # Quantity
    quantity = []
    global quantity_value 
    quantity_value = IntVar()
    for i in range(1,101):
        quantity.append(i)
    quantity_dropdown = Combobox(details_frame,textvariable=quantity_value,font="cambria 15",state=DISABLED)
    quantity_dropdown.grid(row=7,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)
    quantity_dropdown['values'] = quantity
    quantity_dropdown.current(0)


    # Per Cost
    global per_cost 
    per_cost = IntVar()
    per_cost_entry_box = Entry(details_frame,font="cambria 18",state=DISABLED,textvariable=per_cost)
    per_cost_entry_box.grid(row=8,column=1,ipadx=5,ipady=5,pady=5,columnspan=3,sticky=N+E+W+S)

    # For separator Between the entry boxes and labels with the buttons
    Label(details_frame,text="").grid(row=9,column=0)
    Label(details_frame,text="").grid(row=9,column=1)

    # Buttons in details area
    # Creating Add Button
    add_button = Button(details_frame,text="Add",font="Cambria 18",command=lambda : add(text_area),border=5,state=DISABLED)
    add_button.grid(row=10,column=0,sticky=N+E+W+S)

    # Creating Clear Button
    clear_button = Button(details_frame,text="Clear",font="Cambria 18",command=clear,border=5)
    clear_button.grid(row=10,column=1,sticky=N+E+W+S)

    # Creating Reset Button
    reset_button = Button(details_frame,text="Reset",font="Cambria 18",command=lambda : reset(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box),border=5,state=DISABLED)
    reset_button.grid(row=11,column=0,sticky=N+E+W+S)

    # Creating Generate Bill Button
    generate_bill_button = Button(details_frame,text="Generate Bill",font="Cambria 18",command=lambda : generateBill(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box,total_bill_button),border=5)
    generate_bill_button.grid(row=11,column=1,sticky=N+E+W+S)

    # Creating Total Bill Button
    global total_value_list 
    total_value_list = []
    total_bill_button = Button(details_frame,text="  Total  ",font="Cambria 18",command=lambda : total(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box,total_bill_button,save_bill_button),border=5,state=DISABLED)
    total_bill_button.grid(row=10,column=2,rowspan=2,sticky=N+E+W+S)


    # ===============================Billing Section====================================
    billing_frame = Frame(main_frame,border=10,relief=GROOVE,bg="light blue")
    billing_frame.pack(side=RIGHT,anchor=E,fill=Y)

    Label(billing_frame,text="Billing Area",font="mouser 20",border=7,relief=RAISED,padx=5,pady=5).pack(fill=X,padx=5,pady=5)
    Label(billing_frame).pack(fill=X)

    # Text Area of the billing section
    billing_area_frame = Frame(billing_frame)
    billing_area_frame.pack()
    # Scrollbar
    scrollbar = Scrollbar(billing_area_frame)
    scrollbar.pack(side=RIGHT,fill=Y)
    # Text Area
    text_area = Text(billing_area_frame,font="cambria 15",width=70,height=17,yscrollcommand=scrollbar.set,state=NORMAL)
    text_area.pack()
    defaultBill(text_area)
    scrollbar.config(command=text_area.yview)

    Label(billing_frame,text="").pack(fill=X)
    save_bill_button = Button(billing_frame,text="Save Bill",font="Cambria 18",command=lambda : saveBill(text_area.get(1.0,END)),border=5,width=15,state=DISABLED)
    save_bill_button.pack(fill=X,padx=5,pady=5)



# Updating the cost per unit according to the selected item
def updatePerCostValue(event):
    item_value.get()
    per_cost.set(food_menu[item_value.get()])


# Clear Button
def clear():
    customer_name.set("")
    customer_contact.set("")


# Add Button
def add(text_area):
    total_value = per_cost.get() * quantity_value.get()

    text_area.insert(END,f"\n   {item_value.get()}                                  {per_cost.get()}                                   {quantity_value.get()}                                    {total_value}")
    total_value_list.append(total_value)


# Total Button
def total(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box,total_bill_button,save_bill_button):
    per_cost_entry_box.config(state = DISABLED)
    item_dropdown.config(state = DISABLED)
    quantity_dropdown.config(state = DISABLED)
    add_button.config(state = DISABLED)
    reset_button.config(state = NORMAL)

    generate_bill_button.config(state = NORMAL)
    clear_button.config(state = NORMAL)
    customer_contact_entry_box.config(state = NORMAL)
    customer_name_entry_box.config(state = NORMAL)

    grand_total = 0

    for item in total_value_list:
        grand_total = grand_total + item

    print(total_value_list)
    text_area.insert(END,"\n======================================================================")
    text_area.insert(END,f"\n\t\t\t          Total : {grand_total}")
    text_area.insert(END,f"\n\t\t\tGST : 18% of {grand_total} = {(18/100)*grand_total}")
    text_area.insert(END,f"\n\t\t\t     Grand Total : {grand_total + ((18/100)*grand_total)}")
    text_area.insert(END,"\n======================================================================")
    text_area.insert(END,"\t\t\t\t\t**********\t\t\t\t\t\t")

    total_bill_button.config(state = DISABLED)
    generate_bill_button.config(state = DISABLED)
    clear_button.config(state = DISABLED)
    customer_contact_entry_box.config(state = DISABLED)
    customer_name_entry_box.config(state = DISABLED)
    save_bill_button.config(state = NORMAL)
    

# Reset Button
def reset(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box):

    text_area.delete(1.0,END)
    per_cost_entry_box.config(state = DISABLED)
    item_dropdown.config(state = DISABLED)
    quantity_dropdown.config(state = DISABLED)
    add_button.config(state = DISABLED)
    reset_button.config(state = DISABLED)

    generate_bill_button.config(state = NORMAL)
    clear_button.config(state = NORMAL)
    customer_contact_entry_box.config(state = NORMAL)
    customer_name_entry_box.config(state = NORMAL)
    customer_contact.set("")
    customer_name.set("")

    bill_no.set(random.randint(0,1000))
    defaultBill(text_area)


# Saving the bill generated in a text format
def saveBill(text):
    file = fd.asksaveasfile(defaultextension=".txt",filetypes=[("Text File",".txt"),("Pdf File",".pdf"),("All Files",".*")])
    file.write(text)
    file.close()


# The Default bill wwhich will be printed when reset
def defaultBill(text_area):
    text_area.insert(1.0,"======================================================================")
    text_area.insert(END,"\n||                                                                        Manohar Sweets                                                                               ||")
    text_area.insert(END,"\n||                                                                 Main Market, Rudrapur                                                                        ||")
    text_area.insert(END,"\n||                                                                Contact- +917569595656                                                                   ||")
    text_area.insert(END,"\n======================================================================")
    text_area.insert(END,f"  Bill number : {bill_no.get()}")


# Generate Bill - Adding Customer's details(Name,Contact Number)
def generateBill(text_area,per_cost_entry_box,item_dropdown,quantity_dropdown,add_button,reset_button,generate_bill_button,clear_button,customer_name_entry_box,customer_contact_entry_box,total_bill_button):
    text_area.insert(END,f"\n  Customer Name : {customer_name.get()}")
    text_area.insert(END,f"\n  Contact Number : {customer_contact.get()}")
    text_area.insert(END,f"\n  Date : {date.get()}")
    text_area.insert(END,"\n======================================================================")
    text_area.insert(END,"\n   Item Name                                  Cost per unit                                   Quantity                                   Total")
    text_area.insert(END,"\n======================================================================")

    per_cost_entry_box.config(state = NORMAL)
    item_dropdown.config(state = NORMAL)
    quantity_dropdown.config(state = NORMAL)
    add_button.config(state = NORMAL)
    reset_button.config(state = NORMAL)

    generate_bill_button.config(state = DISABLED)
    clear_button.config(state = DISABLED)
    customer_contact_entry_box.config(state = DISABLED)
    customer_name_entry_box.config(state = DISABLED)
    total_bill_button.config(state = NORMAL)


# Create Account Window
def createAccountWindow():

    create_account_window = Toplevel()
    create_account_window.title("Create Account")

    create_window_width = 800
    create_window_height = 500
    create_account_window.geometry(f"{create_window_width}x{create_window_height}")
    create_account_window.minsize(800,500)
    create_account_window.resizable(0,0)

    create_account_frame = Frame(create_account_window,bg="pink",border=5,relief=GROOVE,padx=10,pady=10)
    create_account_frame.pack(side=TOP,anchor=N,fill=X)

    Label(create_account_frame,text="Create Account",bg="yellow",fg="black",width=3,height=3,font="obelixpro 18").pack(fill=X)

    create_account_details_frame = Frame(create_account_window,padx=10,pady=10,bg="pink")
    create_account_details_frame.pack(ipadx=10,ipady=10)

    Label(create_account_details_frame,text="Username : ",font="cambria 20",bg="pink").grid(row=0,column=0,sticky=N+E+W+S,padx=10,pady=10)

    create_username = StringVar()
    create_username_entry = Entry(create_account_details_frame,textvariable=create_username,font="cambria 20")
    create_username_entry.grid(row=0,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

    
    Label(create_account_details_frame,text="Password : ",font="cambria 20",bg="pink").grid(row=1,column=0,sticky=N+E+W+S,padx=10,pady=10)
    create_password = StringVar()
    create_password_entry = Entry(create_account_details_frame,textvariable=create_password,font="cambria 20",show="*")
    create_password_entry.grid(row=1,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

    Button(create_account_details_frame,text="Create",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=lambda : createAccount(create_username.get(),create_password.get(),create_account_window)).grid(row=2,column=0,columnspan=2,ipadx=5,ipady=5,padx=10,pady=10,sticky=N+E+W+S)


# Create Account Logic
def createAccount(create_usr,create_pass,create_account_window):
    db = msc.connect(host="localhost",user="root",passwd="0000")

    db_cursor = db.cursor()
    
    db_cursor.execute("create database if not exists restaurant")
    db_cursor.execute("use restaurant")
    db_cursor.execute("create table if not exists logindetails (username varchar(50),password varchar(50))")

    db_cursor.execute("select username from logindetails")
    
    username_list = []
    value = (create_usr,create_pass)
    for x in db_cursor:
        username_list.append(x[0])

    cmd = "insert into logindetails values(%s,%s)"

    if create_usr in username_list:
        tmsg.showerror("Error","Username Exists! Choose another..")
    else:
        tmsg.showinfo("Congratulations!","Account Created!")
        db_cursor.execute(cmd,value)
        db.commit()
        create_account_window.destroy()

        db_cursor.close()


# Login Account Logic
def loginAccount(log_usr,log_pass):
    db = msc.connect(host="localhost",user="root",passwd="0000")

    db_cursor = db.cursor()
    
    val = (log_usr,log_pass)

    db_cursor.execute("use restaurant")

    db_cursor.execute("select * from logindetails")
    records = db_cursor.fetchall()

    try:
        if val[0]==records[records.index(val)][0] and val[1]==records[records.index(val)][1]:
            tmsg.showinfo("Logged In","Logged In Successfully!")
            db_cursor.close()
            billManagementWindow()
    except:
        tmsg.showerror("Error","Username or password is incorrect!")


    




# ===================================== Main Window Here =====================================

window_width = 800
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.minsize(800,500)
root.resizable(0,0)
root.title("Log In")


login_frame = Frame(root,bg="pink",border=5,relief=GROOVE,padx=10,pady=10)
login_frame.pack(side=TOP,anchor=N,fill=X)

Label(login_frame,text="Log In",font="obelixpro 18",bg="yellow",fg="black",width=3,height=3).pack(fill=X)

login_details_frame = Frame(root,padx=10,pady=10,bg="pink")
login_details_frame.pack(ipadx=10,ipady=10)

Label(login_details_frame,text="Username : ",font="cambria 20",bg="pink").grid(row=0,column=0,sticky=N+E+W+S,padx=10,pady=10)
username = StringVar()
username_entry = Entry(login_details_frame,textvariable=username,font="cambria 20").grid(row=0,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

Label(login_details_frame,text="Password : ",font="cambria 18",bg="pink").grid(row=1,column=0,sticky=N+E+W+S,padx=10,pady=10)
password = StringVar()
password_entry = Entry(login_details_frame,textvariable=password,font="cambria 20",show="*").grid(row=1,column=1,padx=10,pady=10,ipadx=10,ipady=5)


login_button = Button(login_details_frame,text="Log In",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=lambda : loginAccount(username.get(),password.get()))
login_button.grid(row=2,column=0,ipadx=5,ipady=5,padx=10,pady=20)

# Create Account
create_account_button = Button(login_details_frame,text="Create Account",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=createAccountWindow)
create_account_button.grid(row=2,column=1,ipadx=5,ipady=5,padx=10,pady=20)




root.mainloop()
















