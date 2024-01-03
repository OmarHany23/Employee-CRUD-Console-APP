import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta, date


window = Tk()
window.geometry('1506x768')


# Establish a connection to the MySQL database with the specified parameters.
connection_config = {
    'host': 'localhost',
    'password': '1234',
    'user': 'root',
    'database': 'crud'
}
conn = mysql.connector.connect(**connection_config)
# Create a cursor object to interact with the MySQL database.
cursor = conn.cursor()

def execute_query(query, cursor, conn):
    try:
        # Check if the cursor is connected, if not, reconnect.
        if not conn.is_connected():
            conn.reconnect()
            cursor = conn.cursor()
        # Execute the SQL query using the provided cursor.
        cursor.execute(query)

        # Fetch all the rows returned by the query and store them in the 'rows' variable.
        rows = cursor.fetchall()

        # Iterate through each row and print its contents.
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to validate the name entry
name_valid = False
def name_validation (event):
    global name_valid
    emp_name = name_entry.get()
    if len(emp_name) == 0:
        name_validation_msg.config(text="Name Cannot Be Empty!")
    else:
        try:
            if any(char.isdigit() for char in emp_name):
                name_validation_msg.config(text="Name Cannot have numeric!")
            elif emp_name.isspace() or emp_name == "":
                name_validation_msg.config(text="Please enter a Name!")
            elif len(emp_name) <= 2:
                name_validation_msg.config(text="minimum 3 characters required!")
            elif len(emp_name) > 150:
                name_validation_msg.config(text="The Name is too long!")
            else:
                name_validation_msg.config(text="")
                name_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)

# Function to validate Phone entry
phone_valid = False
def phone_validation (event):
    global phone_valid
    emp_phone = phone_entry.get()
    phone_duplicate = False
    if len(emp_phone) == 0:
        Phone_validation_msg.config(text="Phone Cannot Be Empty!")
    else:
        try:
            cursor.execute("SELECT phone FROM crud.employee;")
            phone_rows = cursor.fetchall()
            for row in phone_rows:
                if row[0] == emp_phone:
                    phone_duplicate = True
                    break
            if phone_duplicate:
                Phone_validation_msg.config(text="Phone Number already exists, Enter another one. ")
            elif len(emp_phone) != 11 or not emp_phone.isdigit():
                Phone_validation_msg.config(text="Phone Number Must be 11 numerical values. ")
            else:
                Phone_validation_msg.config(text="")
                phone_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)

# Function to validate Email entry
email_valid = False
def email_validation (event):
    global email_valid
    emp_email = Email_entry.get()
    email_duplicate = False
    if len(emp_email) == 0:
        Email_validation_msg.config(text="Email Cannot Be Empty!")
    else:
        try:
            cursor.execute("SELECT email FROM crud.employee")
            email_rows = cursor.fetchall()
            for row in email_rows:
                if row[0] == emp_email:
                    email_duplicate = True
                    break
            # Count the number of the characters before the @ sign
            y = 0
            for i in range(len(emp_email)):
                if emp_email[i] == '@':
                    break
                else:
                    y=y+1

            if emp_email.count("@") != 1:
                Email_validation_msg.config(text="Email must have only one @, Enter a Valid Email. ")
            elif emp_email.count(".") != 1:
                Email_validation_msg.config(text="Email must have only one '.', Enter a Valid Email. ")
            elif emp_email.find('.') < emp_email.find('@'):
                Email_validation_msg.config(text="The '@' Must come Before the '.' .")
            elif y<3 :
                Email_validation_msg.config(text="Enter at Least Three Characters before the '@' .")
            elif email_duplicate:
                Email_validation_msg.config(text="Email already exists, Please enter another one.")
            else:
                Email_validation_msg.config(text="")
                email_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)

# Function to validate SSN entry
ssn_valid = False
def ssn_validation (event):
    global ssn_valid
    emp_ssn = SSN_entry.get()
    if len(emp_ssn) == 0:
        SSN_validation_msg.config(text="SSN Cannot Be Empty!")
    else:
        try:
            ssn_duplicate = False
            cursor.execute("SELECT ssn FROM crud.employee")
            ssn_rows = cursor.fetchall()
            for row in ssn_rows:
                if str(row[0]) == emp_ssn:
                    ssn_duplicate = True
                    break
            if ssn_duplicate:
                SSN_validation_msg.config(text="Social Security Number already exists, Enter another one.")
            elif len(emp_ssn) != 14 or not emp_ssn.isdigit():
                SSN_validation_msg.config(text="Social Security Number Must be 14 numerical values. ")
            else:
                SSN_validation_msg.config(text="")
                ssn_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)

# Function to validate Address entry
address_valid = False
def address_validation (event):
    global address_valid
    emp_address = Address_entry.get()
    if len(emp_address) == 0:
        Address_validation_msg.config(text="Address Cannot Be Empty!")
    else:
        try:
            if len(emp_address) < 10:
                Address_validation_msg.config(text="Address is too short Enter a Valid Address!")
            elif governorate_options.get() == "Governorates":
                Address_validation_msg.config(text="Choose One of the Governorates!")
                address_valid = True
            else:
                Address_validation_msg.config(text="")
                address_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)
governorate_valid = False
def governorate_list_Select (event):
    global governorate_valid
    emp_address = Address_entry.get()
    if governorate_options.get() == "Governorates":
        Address_validation_msg.config(text="Choose One of the Governorates!")
    elif len(emp_address) < 10:
        Address_validation_msg.config(text="Address is too short Enter a Valid Address!")
    else:
        Address_validation_msg.config(text="")
        governorate_valid = True

# Function to validate Age entry
age_valid = False
def age_validation (event):
    global age_valid
    emp_age = Age_entry.get()
    if len(emp_age) == 0:
        Age_validation_msg.config(text="Please Enter an Age!")
    else:
        try:
            if not emp_age.isdigit():
                Age_validation_msg.config(text="Age Must Be a Numerical Value")
            elif emp_age > '60' or emp_age < '18':
                Age_validation_msg.config(text="Invalid working age, enter an age between 18 and 60. ")
            elif len(emp_age) >2:
                Age_validation_msg.config(text="Invalid age, Age Cannot Be More Than two Digits. ")

            else:
                Age_validation_msg.config(text="")
                age_valid = True
        except Exception as ep:
            messagebox.showerror('error', ep)

# Function to validate Contract Date entry
contract_date_valid = False
def contract_date_validation ():
    global contract_date_valid, view_employees_clicked

    # Enable mostly disabled feilds
    phone_entry.config(state=NORMAL)
    Email_entry.config(state=NORMAL)
    SSN_entry.config(state=NORMAL)
    try:
        if age_valid and Age_entry.get() != '':
            age = int(Age_entry.get())
            birthdate = datetime.now() - timedelta(days=(365.25 * age))
            year, month, day = str(ContractDate_entry.get_date()).split('-')
            contract_date = datetime(int(year), int(month), int(day))
            if contract_date < birthdate + timedelta(days =(365.25 * 18)):
                ContractDate_validation_msg.config(text=f"Invalid Contract Date, Employee was '{(contract_date.year - birthdate.year)}' years old.")
            elif contract_date > datetime.now():
                ContractDate_validation_msg.config(text="Contract date cannot be in the future.")
            else:
                ContractDate_validation_msg.config(text="")
                contract_date_valid = True
        else:
            messagebox.showerror('error', 'PLEASE FILL ALL OF THE FIELDS!!')
    except Exception as ep:
            messagebox.showerror('error', ep)

    if(name_valid and phone_valid and email_valid and ssn_valid and address_valid and governorate_valid and age_valid and contract_date_valid):
        insert_employee = f"INSERT INTO `crud`.`employee` (`name`, `phone`, `address`, `ssn`, `contract_date`, `age`, `email`) VALUES ('{name_entry.get()}', '{phone_entry.get()}', '{Address_entry.get() + ', ' + governorate_options.get() + ', ' + 'Egypt'}', '{SSN_entry.get()}', '{ContractDate_entry.get_date()}', '{int(Age_entry.get())}', '{Email_entry.get()}');"
        cursor.execute(insert_employee)
        conn.commit()
        vmsg.config(text="")

        # Refreshing the Employees Table
        employees_table.delete(*employees_table.get_children())
        view_query = "SELECT * FROM crud.employee;"
        cursor.execute(view_query)
        rows = cursor.fetchall()
        #loop to view the data in the viewing area
        for data in rows:
            employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        view_employees_clicked = True
        # Clear any data in the entry boxes
        name_entry.delete(0,END)
        phone_entry.delete(0,END)
        Email_entry.delete(0,END)
        SSN_entry.delete(0,END)
        Address_entry.delete(0,END)
        Age_entry.delete(0,END)
        governorate_options.set('Governorates')
        ContractDate_entry.set_date(datetime.now())

        print("success")
    else:
        vmsg.config(text="Check all the Required Fields")

# Function to View all the Employees
view_employees_clicked = False
def view_employees ():
    global view_employees_clicked
    # Clear the existing data in the Treeview
    employees_table.delete(*employees_table.get_children())
    view_query = "SELECT * FROM crud.employee;"
    cursor.execute(view_query)
    rows = cursor.fetchall()
    view_employees_clicked =True
    #loop to view the data in the viewing area
    for data in rows:
        employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

# Function to get the selected employee from the view
id = int
Get_emp_clicked = False
def Get_selected ():
    global name_valid,address_valid,age_valid
    if(view_employees_clicked):
        global id
        global Get_emp_clicked
        selected_emp = employees_table.focus()
        details = employees_table.item(selected_emp)
        emp_id = details.get("values")[0]
        id = emp_id
        cursor.execute(f"SELECT name, phone, address, ssn, contract_date, age, email FROM crud.employee WHERE (id= '{emp_id}'); ")
        data = cursor.fetchall()
        for row in data:
            emp_name = row[0]
            emp_phone = row[1]
            emp_address= row[2]
            emp_ssn = row[3]
            emp_contract_date = row[4]
            emp_age = row[5]
            emp_email = row[6]
    
        # Extracting the governate from the address
        address_elements = emp_address.split(', ')
        # Check if any element is a governorate
        found_governorates = [element.title() for element in address_elements if element.title() in Governorates_list]
        governorate_options.set(found_governorates)

        address_list = []
        address_string=""
        for i in address_elements:
            if i.title() in Governorates_list:
                break
            address_list.append(i)
        for row in address_list:
            address_string += ' '+row

        # Clear any data in the entry boxes
        name_entry.delete(0,END)
        phone_entry.delete(0,END)
        Email_entry.delete(0,END)
        SSN_entry.delete(0,END)
        Address_entry.delete(0,END)
        Age_entry.delete(0,END)
        
        # inserting data to the entry boxes
        name_entry.insert(0,emp_name)
        phone_entry.insert(0,emp_phone)
        Email_entry.insert(0,emp_email)
        SSN_entry.insert(0,emp_ssn)
        Address_entry.insert(0,address_string)
        Age_entry.insert(0,emp_age)

        #splitting the contract date
        cyear, cmonth, cday =str(emp_contract_date).split('-')
        ContractDate_entry.set_date(date(int(cyear),int(cmonth),int(cday)))
        Get_emp_clicked = True

        # Disaple uniqe entry values
        phone_entry.config(state=DISABLED)
        Email_entry.config(state=DISABLED)
        SSN_entry.config(state=DISABLED)

        name_valid = False
        address_valid = False
        age_valid = False


    else:
        messagebox.showerror('Usage Error','Cannot get Selection before Viewing Employees and select one.')

# Function to delete an employee
def delete_employee ():
    global id,Get_emp_clicked
    if Get_emp_clicked:
        cursor.execute(f"SELECT name FROM crud.employee WHERE (id= '{id}'); ")
        emp_name = cursor.fetchall()
        for row in emp_name:
            emp_name = row[0]
        confirming = messagebox.askyesno('Confirmation Message',f"Are You sure you want to delete '{emp_name}'")
        if confirming:
            cursor.execute(f"DELETE FROM crud.employee WHERE (id = '{id}')")
            conn.commit()
            
            # Refreshing the Employees Table
            employees_table.delete(*employees_table.get_children())
            view_query = "SELECT * FROM crud.employee;"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            
            # Enable mostly disabled feilds
            phone_entry.config(state=NORMAL)
            Email_entry.config(state=NORMAL)
            SSN_entry.config(state=NORMAL)

            # Clear any data in the entry boxes
            name_entry.delete(0,END)
            phone_entry.delete(0,END)
            Email_entry.delete(0,END)
            SSN_entry.delete(0,END)
            Address_entry.delete(0,END)
            Age_entry.delete(0,END)
            governorate_options.set('Governorates')
            ContractDate_entry.set_date(datetime.now())
            Get_emp_clicked = False

            


    else:
        messagebox.showerror('Usage Error','Cannot Delete an Employee Before Selecting one.')

# Function to Update an employee

def update_employee ():
    global name_valid,address_valid,age_valid,id,Get_emp_clicked

    if name_valid and address_valid and age_valid:
        if Get_emp_clicked:
            global id
            get_governorate = governorate_options.get()
            mapping_table = str.maketrans({'(':'', ')':'', ',':'', "'":''})
            new_governorate = get_governorate.translate(mapping_table)
            update_employee = """
                                UPDATE `crud`.`employee`
                                SET 
                                    `name` = %s,
                                    `address` = %s,
                                    `contract_date` = %s,
                                    `age` = %s
                                WHERE
                                    `id` = %s;
                            """
            employee_data = (
                name_entry.get(),
                f"{Address_entry.get() + ', ' + new_governorate + ', ' + 'Egypt'}",
                ContractDate_entry.get_date(),
                int(Age_entry.get()),
                id  # replace with the actual value for id
            )

            cursor.execute(update_employee, employee_data)
            conn.commit()
            
            # Enable mostly disabled feilds
            phone_entry.config(state=NORMAL)
            Email_entry.config(state=NORMAL)
            SSN_entry.config(state=NORMAL)

            # Clear Entry Widgets
            name_entry.delete(0,END)
            phone_entry.delete(0,END)
            Email_entry.delete(0,END)
            SSN_entry.delete(0,END)
            Address_entry.delete(0,END)
            Age_entry.delete(0,END)
            governorate_options.set('Governorates')
            ContractDate_entry.set_date(datetime.now())

            # Refreshing the Employees Table
            employees_table.delete(*employees_table.get_children())
            view_query = "SELECT * FROM crud.employee;"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

            vmsg.config(text="")
            id = ''
            Get_emp_clicked = False
        else:
            messagebox.showerror('Usage Error','Cannot Update an Employee Before Selecting one.')
    else:
        messagebox.showerror('Usage Error','Please Reenter the data.')
        vmsg.config(text="Check all the Required Fields")
# Function to Reset entry widgets
def reset_values ():
        global id,Get_emp_clicked,view_employees_clicked
    # Enable mostly disabled feilds
        phone_entry.config(state=NORMAL)
        Email_entry.config(state=NORMAL)
        SSN_entry.config(state=NORMAL)

        # Clear Entry Widgets
        name_entry.delete(0,END)
        phone_entry.delete(0,END)
        Email_entry.delete(0,END)
        SSN_entry.delete(0,END)
        Address_entry.delete(0,END)
        Age_entry.delete(0,END)
        search_entry.delete(0,END)
        governorate_options.set('Governorates')
        ContractDate_entry.set_date(datetime.now())
        search_options.set('Search By')


        # Clearing all of the validation messages
        name_validation_msg.config(text="")
        Phone_validation_msg.config(text="")
        Email_validation_msg.config(text="")
        SSN_validation_msg.config(text="")
        Address_validation_msg.config(text="")
        Age_validation_msg.config(text="")
        ContractDate_validation_msg.config(text="")
        vmsg.config(text="")
        search_validation_msg.config(text="")

        #resetting global values
        id = 0
        Get_emp_clicked = False
        view_employees_clicked = False

        # Clear the View Table
        employees_table.delete(*employees_table.get_children())


# Function to validate the search
def search_employees():
    global view_employees_clicked
    if search_options.get() == "Search By":
        search_validation_msg.config(text="Choose One of the Searching Options!")
    else:
        view_employees_clicked = True
        if search_options.get() == "ID":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where (id='{search_entry.get()}%');"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "Name":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where name like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
                
        elif search_options.get() == "Phone":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where phone like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "Address":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where address like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "SSN":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where ssn like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "Age":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where age like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "Email":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where email like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        elif search_options.get() == "Contract Date":
            # Clear the existing data in the Treeview
            employees_table.delete(*employees_table.get_children())
            view_query = f"SELECT * FROM crud.employee where contract_date like '%{search_entry.get()}%';"
            cursor.execute(view_query)
            rows = cursor.fetchall()
            #loop to view the data in the viewing area
            for data in rows:
                employees_table.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

        else:
            pass
        search_validation_msg.config(text="")


titlef = ('sans-serif', 18)
warningf = ('sans-serif', 10)

mainFrame = LabelFrame(window, text="Main Frame", padx=5, pady=5)
mainFrame.grid(row=0,column=0,padx=10,pady=10)

viewFrame = LabelFrame(window, text="View Employees Frame", padx=5, pady=5)
viewFrame.grid(row=0,column=1,padx=10,pady=10)

buttonsFrame = LabelFrame(window, text="", padx=5, pady=5)
buttonsFrame.grid(row=1,column=0,padx=10,pady=10)

searchFrame = LabelFrame(window, text="", padx=5, pady=5)
searchFrame.grid(row=1,column=1,padx=10,pady=10)

# Message on the left of the name entry box
name_msg = Label(mainFrame, text='Name:', font=titlef)
name_msg.grid(row=0, column=0, padx=0, pady=0)
# Name entry box
name_entry = Entry(mainFrame, width=16, font=titlef)
name_entry.bind('<FocusOut>', name_validation)
name_entry.grid(row=0, column=1, padx=0, pady=5)
# Validation message for the name entry
name_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
name_validation_msg.grid(row=0, column=2, padx=0, pady=0)

# Message on the left of the Phone entry box
phone_msg = Label(mainFrame, text='Phone:', font=titlef)
phone_msg.grid(row=1, column=0, padx=0, pady=0)
# Phone Entry Box
phone_entry = Entry(mainFrame, font=titlef)
phone_entry.bind('<FocusOut>', phone_validation)
phone_entry.grid(row=1, column=1, padx=10, pady=10)
# Validation message for the Phone entry
Phone_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
Phone_validation_msg.grid(row=1, column=2, padx=0, pady=0)

# Message on the left of the Email entry box
Email_msg = Label(mainFrame, text='Email:', font=titlef)
Email_msg.grid(row=2, column=0, padx=0, pady=0)
# Email Entry Box
Email_entry = Entry(mainFrame, font=titlef)
Email_entry.bind('<FocusOut>', email_validation)
Email_entry.grid(row=2, column=1, padx=10, pady=10)
# Validation message for the Email entry
Email_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
Email_validation_msg.grid(row=2, column=2, padx=0, pady=0)

# Message on the left of the SSN entry box
SSN_msg = Label(mainFrame, text='SSN:', font=titlef)
SSN_msg.grid(row=3, column=0, padx=0, pady=0)
# SSN Entry Box
SSN_entry = Entry(mainFrame, font=titlef)
SSN_entry.bind('<FocusOut>', ssn_validation)
SSN_entry.grid(row=3, column=1, padx=10, pady=10)
# Validation message for the SSN entry
SSN_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
SSN_validation_msg.grid(row=3, column=2, padx=0, pady=0)

# Message on the left of the Address entry box
Address_msg = Label(mainFrame, text='Address:', font=titlef)
Address_msg.grid(row=4, column=0, padx=0, pady=0)
# Address Entry Box
Address_entry = Entry(mainFrame, font=titlef)
Address_entry.bind('<FocusOut>', address_validation)
Address_entry.grid(row=4, column=1, padx=10, pady=10)
# Validation message for the Address entry
Address_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
Address_validation_msg.grid(row=4, column=2, padx=0, pady=0)
# Adding Address's Governorate List
Governorates_list =["Cairo", "Giza", "Alexandria", "Beheira", "Beni Suef",
                    "Aswan", "Dakahlia", "Damietta", "Fayoum", "Gharbia",
                    "Assiut", "Ismailia", "Kafr el-Sheikh", "Matrouh", "Minya",
                    "Menofia", "New Valley", "North Sinai", "Port Said", "Qualyubia", 
                    "Qena", "Red Sea", "Al-Sharqia", "Soha", "South Sinai", "Suez", "Luxor"]

governorate_options=StringVar(mainFrame)
governorate_options.set('Governorates')
governorate_list = OptionMenu(mainFrame,governorate_options,*Governorates_list,command=governorate_list_Select)
governorate_list.grid(row=4,column=3)

# Message above Age entry box
Age_msg = Label(mainFrame, text='Age:', font=titlef)
Age_msg.grid(row=5, column=0, padx=0, pady=0)
# Age Entry Box
Age_entry = Entry(mainFrame, font=titlef)
Age_entry.bind('<FocusOut>', age_validation)
Age_entry.grid(row=5, column=1, padx=10, pady=10)
# Validation message for the Age entry
Age_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
Age_validation_msg.grid(row=5, column=2, padx=0, pady=0)

# Message on the left of the ContractDate entry box
ContractDate_msg = Label(mainFrame, text='Contract-Date:', font=titlef)
ContractDate_msg.grid(row=6, column=0, padx=0, pady=0)
# ContractDate Entry Box
# ContractDate_entry = Entry(window, font=titlef)
ContractDate_entry = DateEntry(mainFrame,selectmode='day')
ContractDate_entry.set_date(datetime.now())
ContractDate_entry.grid(row=6, column=1, padx=10, pady=10)
# Validation message for the ContractDate entry
ContractDate_validation_msg = Label(mainFrame, text='', fg='red', font=warningf)
ContractDate_validation_msg.grid(row=6, column=2, padx=0, pady=0)

# Creating Create New Employee Button
vmsg=Label(mainFrame, text='', fg='red', font=warningf)
vmsg.grid(row=7, column=1,pady=50)
create_new_emp = Button(buttonsFrame, text='Create New',command=contract_date_validation)
create_new_emp.grid(row=0,column=1,padx=10,pady=10)

# Viewing all of the employees datas
view_emp = Button(buttonsFrame, text='View Employees',command=view_employees)
view_emp.grid(row=0,column=2,padx=10,pady=10)

employees_table = ttk.Treeview(viewFrame,selectmode='browse')
employees_table.grid(row=1,column=0,padx=20,pady=20)
employees_table["columns"]=["1","2","3","4","5","6","7","8"]
employees_table['show']=['headings']
employees_table.column("1",width=5,anchor='c')
employees_table.column("2",width=85,anchor='c')
employees_table.column("3",width=85,anchor='c')
employees_table.column("4",width=205,anchor='c')
employees_table.column("5",width=95,anchor='c')
employees_table.column("6",width=83,anchor='c')
employees_table.column("7",width=30,anchor='c')
employees_table.column("8",width=220,anchor='c')
employees_table.heading("1",text="ID")
employees_table.heading("2",text="Name")
employees_table.heading("3",text="Phone")
employees_table.heading("4",text="Address")
employees_table.heading("5",text="SSN")
employees_table.heading("6",text="Contract_Date")
employees_table.heading("7",text="Age")
employees_table.heading("8",text="Email")

# Getting Employee's Data From the Table
Get_emp = Button(viewFrame, text='Get Selected Employee',command=Get_selected)
Get_emp.grid(row=2,column=0)

# Search for an Employee by selected data
# Search Entry
search_entry = Entry(searchFrame, font=titlef)
search_entry.bind('<FocusOut>', search_employees)
search_entry.grid(row=0, column=0, padx=10, pady=10)
# Search List Of Values
searchs_list =["ID", "Name", "Phone", "Address", "SSN",
                    "Contract Date", "Age", "Email"]
search_options=StringVar(searchFrame)
search_options.set('Search By')
search_list = OptionMenu(searchFrame,search_options,*searchs_list)
search_list.grid(row=0,column=1)
# Search Validation Message
search_validation_msg=Label(searchFrame, text='', fg='red', font=warningf)
search_validation_msg.grid(row=1, column=1,pady=5)
# Search Button
search_button = Button(searchFrame, text='Search',command=search_employees)
search_button.grid(row=0,column=2,padx=10,pady=10)

# Creating a Button to delete an employee
delete_emp = Button(buttonsFrame, text='Delete Employee',command=delete_employee)
delete_emp.grid(row=0,column=4,padx=10,pady=10)

# Creating a Button to Update an Employee
update_emp = Button(buttonsFrame, text='Update Employee',command=update_employee)
update_emp.grid(row=0,column=3,padx=10,pady=10)

# Creating a Button to Clear entry widgets values
reset_button = Button(buttonsFrame, text='RESET',command=reset_values)
reset_button.grid(row=0,column=0,padx=10,pady=10)

window.mainloop()
