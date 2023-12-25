import mysql.connector
from datetime import datetime, timedelta

# To authenticate employee data upon acquisition.
class EmployeeValidator:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def validate_name(self):
        while True:
            try:
                emp_name = input("Enter Employee Name: ")
                if any(char.isdigit() for char in emp_name):
                    raise ValueError("Names cannot contain numbers. Enter a valid name. ")
                elif emp_name.isspace() or emp_name == "":
                    print("Please enter a Name.")
                else:
                    break
            except ValueError as e:
                print(e)
        return emp_name

    def validate_phone(self):
        while True:
            try:
                phone_duplicate = False
                emp_phone = input("Enter Employee's Phone: ")
                self.cursor.execute("SELECT phone FROM crud.employee;")
                phone_rows = self.cursor.fetchall()
                for row in phone_rows:
                    if row[0] == emp_phone:
                        phone_duplicate = True
                        break
                if phone_duplicate:
                    print("Phone Number already exists, Enter another one. ")
                elif len(emp_phone) != 11 or not emp_phone.isdigit():
                    print("Phone Number Must be 11 numerical values. ")
                else:
                    break
            except ValueError as e:
                print(e)
        return emp_phone

    def validate_address(self):
        while True:
            try:
                building = input(
                    "Insert -a- if your building is a Primary one\nand -b- if it is a redundant building: ")
                if building in ('a', 'b'):
                    break
                else:
                    raise ValueError("Invalid input.")
            except ValueError as e:
                print(e)

        while True:
            try:
                building_number = int(input("Enter Building Number: "))
                break
            except ValueError:
                print("Wrong input. Please insert a numerical value.")

        while True:
            try:
                street_name = input("Enter Street Name: ")
                if street_name == " " or street_name == "":
                    print("Please enter a Street Name.")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                city = input("Enter the City: ").lower()
                numbers = [num for num in city if num.isdigit()]
                if numbers:
                    raise ValueError("City Names cannot contain numbers. Enter a valid City name. ")
                elif city == " " or city == "":
                    print("Please enter a City Name.")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                country = input("Enter the Country: ").lower()
                numbers = [num for num in country if num.isdigit()]
                if numbers:
                    raise ValueError("Country Names cannot contain numbers. Enter a valid Country name. ")
                elif country == " " or country == "":
                    print("Please enter a Country Name.")
                else:
                    break
            except ValueError as e:
                print(e)

        if building == 'a':
            building = ''
        else:
            building = 'B'

        emp_address = f"{building_number}{building}, {street_name}, {city}, {country}."
        return emp_address

    def validate_ssn(self):
        while True:
            try:
                ssn_duplicate = False
                emp_ssn = input("Enter Employee's SSN: ")
                self.cursor.execute("SELECT ssn FROM crud.employee")
                ssn_rows = self.cursor.fetchall()
                for row in ssn_rows:
                    if str(row[0]) == emp_ssn:
                        ssn_duplicate = True
                        break
                if ssn_duplicate:
                    print("Social Security Number already exists, Enter another one.")
                elif len(emp_ssn) != 14 or not emp_ssn.isdigit():
                    print("Social Security Number Must be 14 numerical values. ")
                else:
                    break
            except ValueError:
                print("Invalid Social Security Number, Please enter a valid one")
        return emp_ssn

    def validate_age(self):
        while True:
            try:
                age = int(input("Enter Employee's age: "))
                if age > 60 or age < 18:
                    print("Invalid working age, enter an age between 18 and 60. ")
                else:
                    break
            except ValueError:
                print("Age must be a Numerical Value. ")
        return age

    def validate_contract_date(self, birthdate):
        while True:
            try:
                year = int(input("Enter Contract year: "))
                month = int(input("Enter Contract Month: "))
                day = int(input("Enter Contract Day: "))
                
                contract_date = datetime(year, month, day)

                if contract_date < birthdate + timedelta(days =(365.25 * 18)):
                    print(f"Invalid Contract Date, Employee was '{(contract_date.year - birthdate.year)}' years old.")
                elif contract_date > datetime.now():
                    print("Contract date cannot be in the future.")
                else:
                    break
            except ValueError:
                print("Invalid date, please enter a valid date.")

        return f"{year}-{month}-{day}"

    def validate_email(self):
        while True:
            try:
                email_duplicate = False
                email = input("Enter Employee's Email: ")
                self.cursor.execute("SELECT email FROM crud.employee")
                email_rows = self.cursor.fetchall()
                for row in email_rows:
                    if row[0] == email:
                        email_duplicate = True
                        break
                if email.count("@") != 1 :#or email.count(".com") != 1
                    print("Email must have one @. ")#and one '.com', Enter a Valid Email. 
                elif email_duplicate:
                    print("Email already exists, Please enter another one.")
                else:
                    # Additional validation for the domain
                    domain = email.split("@")[1]
                    valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr", "gmx.de", "web.de", "yandex.ru", "ymail.com", "libero.it", "outlook.com", "uol.com.br", "bol.com.br", "mail.ru", "cox.net", "hotmail.it", "sbcglobal.net", "sfr.fr", "live.fr", "verizon.net", "live.co.uk", "googlemail.com", "yahoo.es", "ig.com.br", "live.nl", "bigpond.com", "terra.com.br", "yahoo.it", "neuf.fr", "yahoo.de", "alice.it", "rocketmail.com", "att.net", "laposte.net", "facebook.com", "bellsouth.net", "yahoo.in", "hotmail.es", "arcom.com.eg"]  # Add valid domains as needed
                    if domain not in valid_domains:
                        raise ValueError("Invalid email domain. Enter a valid email with an allowed domain.")
                    break
            except ValueError as e:
                print(e)
        return email

    def insert_employee(self, emp_name, emp_phone, emp_address, emp_ssn, contract_date, age, emp_email):
        insert_employee_query = f"INSERT INTO `crud`.`employee` (`name`, `phone`, `address`, `ssn`, `contract_date`, `age`, `email`) VALUES ('{emp_name}', '{emp_phone}', '{emp_address}', '{emp_ssn}', '{contract_date}', '{age}', '{emp_email}');"
        self.cursor.execute(insert_employee_query)
        self.conn.commit()

# Overseeing and handling direct database interactions.
class EmployeeManager:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def execute_query(self, query):
        try:
            # Check if the cursor is connected, if not, reconnect.
            if not self.conn.is_connected():
                self.conn.reconnect()
                self.cursor = self.conn.cursor()
            # Execute the SQL query using the provided cursor.
            self.cursor.execute(query)

            # Fetch all the rows returned by the query and store them in the 'rows' variable.
            rows = self.cursor.fetchall()

            # Iterate through each row and print its contents.
            for row in rows:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def show_all_data(self):
        header = "'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'"
        print("=" * len(header))
        print(header)
        print("=" * len(header))

        show_all_data_query = "SELECT * FROM crud.employee"
        self.execute_query(show_all_data_query)

# Updating employee's Data
class EmployeeUpdater:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
        self.validator = EmployeeValidator(cursor, conn) # Creating an instance of EmployeeValidator
    def _validate_id(self, update_id):
        while True:
            try:
                id_exists = False
                self.cursor.execute("SELECT id FROM crud.employee; ")
                employee_ids = self.cursor.fetchall()
                for row in employee_ids:
                    if row[0] == update_id:
                        id_exists = True
                        break
                if not id_exists:
                    print("Please Enter an Existing Employee's ID")
                else:
                    break
            except ValueError:
                print("Invalid Value, Please Enter a Valid ID")

    def _update_name(self, update_id):
        self.cursor.execute(f"SELECT name FROM crud.employee WHERE (id= '{update_id}'); ")
        old_name = self.cursor.fetchall()
        print("The Old Name is : ", old_name)
        while True:
            try:
                new_name = input("Enter the new Name: ")
                numbers = [num for num in new_name if num.isdigit()]
                if numbers:
                    raise ValueError("Names cannot contain numbers. Enter a valid name: ")
                elif new_name == " " or new_name == "":
                    print("Please enter a Name.")
                else:
                    break
            except ValueError as e:
                print(e)
        self.cursor.execute(f"UPDATE crud.employee SET name = '{new_name}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_phone(self, update_id):
        self.cursor.execute(f"SELECT phone FROM crud.employee WHERE (id= '{update_id}'); ")
        old_phone = self.cursor.fetchall()
        print("The Old Phone Number is : ", old_phone)
        while True:
            try:
                phone_duplicate = False
                new_phone = input("Enter the new Employee's Phone : ")
                self.cursor.execute("SELECT phone FROM crud.employee;")
                phone_rows = self.cursor.fetchall()
                for row in phone_rows:
                    if row[0] == new_phone:
                        phone_duplicate = True
                        break
                if phone_duplicate:
                    print("Phone Number already exists, Enter another one. ")
                elif len(new_phone) != 11 or not new_phone.isdigit():
                    print("Phone Number Must be 11 numerical values: ")
                else:
                    break
            except ValueError as e:
                print(e)
        self.cursor.execute(f"UPDATE crud.employee SET phone = '{new_phone}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_address(self, update_id):
        self.cursor.execute(f"SELECT address FROM crud.employee WHERE (id= '{update_id}'); ")
        old_address = self.cursor.fetchall()
        print("The Old Address Number is : ", old_address)
        while True:
            while True:
                try:
                    building = input("Insert -a- if your building is a Primary one\n and -b- if it is a redundant building: ")
                    if building in ('a', 'b'):
                        break
                    else:
                        raise ValueError("Invalid input.")
                except ValueError as e:
                    print(e)

            while True:
                try:
                    building_number = int(input("Enter Building Number: "))
                    break
                except ValueError:
                    print("Wrong input. Please insert a numerical value.")

            while True:
                try:
                    street_name = input("Enter Street Name: ")
                    if street_name == " " or street_name == "":
                        print("Please enter a Street Name.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    city = input("Enter the City: ").lower()
                    numbers = [num for num in city if num.isdigit()]
                    if numbers:
                        raise ValueError("City Names cannot contain numbers. Enter a valid City name. ")
                    elif city == " " or city == "":
                        print("Please enter a City Name.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    country = input("Enter the Country: ").lower()
                    numbers = [num for num in country if num.isdigit()]
                    if numbers:
                        raise ValueError("Country Names cannot contain numbers. Enter a valid Country name. ")
                    elif country == " " or country == "":
                        print("Please enter a Country Name.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            if building == 'a':
                building = ''
            else:
                building = 'B'

            new_address = str(building_number) + building + ", " + street_name + ", " + city + ", " + country + "."

            self.cursor.execute(f"UPDATE crud.employee SET address = '{new_address}' WHERE (id = '{update_id}')")
            self.conn.commit()
            break

    def _update_ssn(self, update_id):
        self.cursor.execute(f"SELECT ssn FROM crud.employee WHERE (id= '{update_id}'); ")
        old_ssn = self.cursor.fetchall()
        print("The Old Social Security Number is : ", old_ssn)
        while True:
            try:
                ssn_duplicate = False
                new_ssn = input("Enter Employee's SSN : ")
                self.cursor.execute("SELECT ssn FROM crud.employee")
                ssn_rows = self.cursor.fetchall()
                for row in ssn_rows:
                    if str(row[0]) == new_ssn:
                        ssn_duplicate = True
                        break
                if ssn_duplicate:
                    print("Social Security Number already exists, Enter another one.")
                elif len(new_ssn) != 14 or not new_ssn.isdigit():
                    print("Social Security Number Must be 14 numerical values. ")
                else:
                    break
            except ValueError:
                print("invalid Social Security Number, Please enter a valid one.")

        self.cursor.execute(f"UPDATE crud.employee SET ssn = '{new_ssn}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_contract_date(self, update_id):
        self.cursor.execute(f"SELECT contract_date FROM crud.employee WHERE (id= '{update_id}'); ")
        old_contract_date = self.cursor.fetchall()
        print("The Old Contract-Date is : ", old_contract_date)
        self.cursor.execute(f"SELECT age FROM crud.employee WHERE (id= '{update_id}'); ")
        getAge = str(self.cursor.fetchall())
        age = int(''.join([char for char in getAge if char.isdigit()]))
        while True:
            try:
                year = int(input("Enter new Contract year: "))
                if year > 2023 or year < 1981:
                    raise ValueError
                elif year < 2023 - (age - 18):
                    print(f"Invalid Year Employee was '{year - (2023 - age)}' Then, Enter a Valid Year.")
                else:
                    break
            except ValueError:
                print("Invalid year, Enter a Valid year. ")

        while True:
            try:
                month = int(input("Enter Contract Month: "))
                if month > 12 or month < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid month, Enter a Valid Month. ")

        while True:
            try:
                day = int(input("Enter Contract Day: "))
                if day > 31 or day < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid day, Enter a Valid Day. ")

        new_contract_date = str(year)+'-'+str(month)+'-'+str(day)
        self.cursor.execute(f"UPDATE crud.employee SET contract_date = '{new_contract_date}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_age(self, update_id):
        self.cursor.execute(f"SELECT age FROM crud.employee WHERE (id= '{update_id}'); ")
        getAge = str(self.cursor.fetchall())
        old_age = int(''.join([char for char in getAge if char.isdigit()]))
        print("The Old age is : ", old_age)
        self.cursor.execute(f"SELECT contract_date FROM crud.employee WHERE (id= '{update_id}'); ")
        contract_date = str(self.cursor.fetchall())
        contract_date_int = str(''.join([char for char in contract_date if char.isdigit()]))
        contract_year = int(contract_date_int[:4])
        while True:
            try:
                new_age = int(input("Enter new Employee's age: "))
                if new_age > 60 or new_age < 18:
                    print("Invalid working age, enter an age between 18 and 60. ")
                elif (2023 - (contract_year - 18)) > new_age:
                    print(f"Invalid Age Employee must be at least '{2023 - (contract_year - 18)}' to work at '{contract_year}'. ")
                else:
                    break
            except ValueError:
                print("Age must be a Numerical Value. ")

        self.cursor.execute(f"UPDATE crud.employee SET age = '{new_age}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_email(self, update_id):
        self.cursor.execute(f"SELECT email FROM crud.employee WHERE (id= '{update_id}'); ")
        old_email = self.cursor.fetchall()
        print("The Old Email is : ", old_email)
        while True:
            try:
                email_duplicate = False
                new_email = input("Enter Employee's Email: ")
                self.cursor.execute("SELECT email FROM crud.employee")
                email_rows = self.cursor.fetchall()
                for row in email_rows:
                    if row[0] == new_email:
                        email_duplicate = True
                        break
                if new_email.count("@") != 1 :#or email.count(".com") != 1
                    print("Email must have one @. ")#and one '.com', Enter a Valid Email. 
                elif email_duplicate:
                    print("Email already exists, Please enter another one.")
                else:
                    # Additional validation for the domain
                    domain = new_email.split("@")[1]
                    valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr", "gmx.de", "web.de", "yandex.ru", "ymail.com", "libero.it", "outlook.com", "uol.com.br", "bol.com.br", "mail.ru", "cox.net", "hotmail.it", "sbcglobal.net", "sfr.fr", "live.fr", "verizon.net", "live.co.uk", "googlemail.com", "yahoo.es", "ig.com.br", "live.nl", "bigpond.com", "terra.com.br", "yahoo.it", "neuf.fr", "yahoo.de", "alice.it", "rocketmail.com", "att.net", "laposte.net", "facebook.com", "bellsouth.net", "yahoo.in", "hotmail.es", "arcom.com.eg"]  # Add valid domains as needed
                    if domain not in valid_domains:
                        raise ValueError("Invalid email domain. Enter a valid email with an allowed domain.")
                    break
            except ValueError as e:
                print(e)

        self.cursor.execute(f"UPDATE crud.employee SET email = '{new_email}' WHERE (id = '{update_id}')")
        self.conn.commit()

    def _update_all(self, update_id):
        self._update_name( update_id)
        self._update_phone( update_id)
        self._update_address( update_id)
        self._update_ssn(update_id)
        self._update_contract_date(update_id)
        self._update_age(update_id)
        self._update_email(update_id)

    def update_employee(self):
        
        update_id = int(input("Enter The Employee's ID that Needed To be Updated: "))
        self._validate_id(update_id)

        while True:
            print("'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'")
            self.cursor.execute(f"SELECT name, phone, address, ssn, contract_date, age, email FROM crud.employee WHERE (id= '{update_id}'); ")
            old_data = self.cursor.fetchall()
            print(old_data)
            
            update_selection = int(input("To Update the Name enter -1- \n" 
                                         "To Update the Phone Number enter -2- \n"
                                         "To Update the Address enter -3- \n"
                                         "To Update the SSN enter -4- \n"
                                         "To Update the Contract Date enter -5- \n"
                                         "To Update the Age enter -6- \n"
                                         "To Update the Email enter -7- \n"
                                         "To Update All of the Employee information enter -8- \n"
                                         "To Exit enter -0- \n"
                                         "Enter Your Selection : "))
            
            match update_selection:
                case 1:
                    self._update_name(update_id)
                case 2:
                    self._update_phone(update_id)
                case 3:
                    self._update_address(update_id)
                case 4:
                    self._update_ssn(update_id)
                case 5:
                    self._update_contract_date(update_id)
                case 6:
                    self._update_age(update_id)
                case 7:
                    self._update_email(update_id)
                case 8:
                    self._update_all(update_id)
                    pass
                case 0:
                    break
                case _:
                    print("Invalid Selection")

# Deleting whole Employee's Data
class EmployeeDeleter:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.db_manager = EmployeeManager(self.cursor,self.conn)

    def delete_employee(self):
        while True:
            try:
                idExists = False
                deleteID = int(input("Enter The Employee's ID that Needed To be Deleted :"))
                self.cursor.execute("SELECT id FROM crud.employee; ")
                employeeIDs = self.cursor.fetchall()
                for row in employeeIDs:
                    if row[0] == deleteID:
                        idExists = True
                        break
                if idExists == False:
                    print("Please Enter an Existing Employee's ID")
                else:
                    break
            except ValueError:
                print("Invalid Value, Please Enter a Valid ID")

        self.db_manager.execute_query(f"SELECT * FROM crud.employee WHERE (id= '{deleteID}'); ")
        while True:
            try:
                deleteConfirmation = input("Are you sure you want to delete (y/n):")
                if deleteConfirmation in ('y', 'n'):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input.")
        match deleteConfirmation:
            case 'y':
                self.cursor.execute(f"DELETE FROM crud.employee WHERE (id = '{deleteID}')")
                self.conn.commit()
                print("employee Deleted Succesfully.")
            case 'n':
                print("Back To the Main Menu.......")
            case _:
                print("Unexpected Error, Please Restart the application")


def main():
    try:
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

    except Exception as e:
        print(f"An error occurred: {e}")

    while True:
        while True:
            try:
                choice = input(
                    "Enter 1 to Create a new Employee\n"
                    "Enter 2 to View all Employees\n"
                    "Enter 3 to Update an Employee\n"
                    "Enter 4 to Delete an Employee\n"
                    "Enter 5 to Exit\n"
                    "Enter Your Selection: ")
                
                if not choice.isdigit():
                    raise ValueError("Invalid input, Enter a number for the Selection.")

                choice = int(choice)

                if choice in (1, 2, 3, 4, 5):
                    break
                else:
                    raise ValueError("Invalid input, Enter one of the Selection.")
            except ValueError as e:
                print(f"Error: {e}")
        match choice:
            # Creating an Employee Case
            case 1:
                # Create an instance of EmployeeValidator
                validator = EmployeeValidator(cursor, conn)

                # Validate and get employee information
                emp_name = validator.validate_name()
                emp_phone = validator.validate_phone()
                emp_address = validator.validate_address()
                emp_ssn = validator.validate_ssn()
                age = validator.validate_age()

                # Calculate birthdate based on age
                birthdate = datetime.now() - timedelta(days=(365.25 * age))

                # Validate and get contract date
                contract_date = validator.validate_contract_date(birthdate)

                emp_email = validator.validate_email()

                # Insert employee into the database
                validator.insert_employee(emp_name, emp_phone, emp_address, emp_ssn, contract_date, age, emp_email)

            # Viewing Employee's information
            case 2:
                # Create an instance of EmployeeManager
                employee_manager = EmployeeManager(cursor, conn)

                # Show all employee data
                employee_manager.show_all_data()

            # Updating Employee's Information
            case 3:
                # Create an instance of EmployeeManager
                employee_manager = EmployeeManager(cursor, conn)

                # Show all employee data
                employee_manager.show_all_data()

                #Update employee's Data
                updater = EmployeeUpdater(cursor, conn)
                updater.update_employee()

            # Deleting Employee
            case 4:
                # Create an instance of EmployeeManager
                employee_manager = EmployeeManager(cursor, conn)

                # Show all employee data
                employee_manager.show_all_data()
                
                deleter = EmployeeDeleter(conn)
                deleter.delete_employee()

            # Exiting from the Application
            case 5:
                print("Closing Application.......")
                break

            #Handling Unexpected match errors
            case _:
                print("Unexpected Error, Please Restart the application")  

if __name__ == "__main__":
    main()