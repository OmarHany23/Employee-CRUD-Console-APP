import mysql.connector

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

status = True
while status:
    while True:
        try:
            choice = int(input(
                "Enter -1- to Create a new Employee\nEnter -2- to View all Employees\nEnter -3- to Update an Employee\nEnter -4- to Delete an Employee\nEnter -5- to Exit\nEnter Your Selection: "))
            if choice in (1, 2, 3, 4, 5):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, Enter one of the Selection. ")

    match choice:
        # Creating an Employee Case
        case 1:
            print("=================================================================================")
            # Employee name input
            while True:
                try:
                    emp_name = input("Enter Employee Name: ")
                    numbers = [num for num in emp_name if num.isdigit()]
                    if numbers:
                        raise ValueError("Names cannot contain numbers. Enter a valid name. ")
                    elif emp_name == " " or emp_name == "":
                        print("Please enter a Name.")
                    else:
                        break
                except ValueError as e:
                    print(e)
            # Employee Phone number input
            while True:
                try:
                    phone_duplicate = False
                    emp_phone = input("Enter Employee's Phone: ")
                    cursor.execute("SELECT phone FROM crud.employee;")
                    phone_rows = cursor.fetchall()
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
            # Employee Address input
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

            emp_address = str(building_number) + building + ", " + street_name + ", " + city + ", " + country + "."
            # Employee's SSN
            while True:
                try:
                    ssn_duplicate = False
                    emp_ssn = input("Enter Employee's SSN: ")
                    cursor.execute("SELECT ssn FROM crud.employee")
                    ssn_rows = cursor.fetchall()
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

            # Employee's age
            while True:
                try:
                    age = int(input("Enter Employee's age: "))
                    if age > 60 or age < 18:
                        print("Invalid working age, enter an age between 18 and 60. ")
                    else:
                        break
                except ValueError:
                    print("Age must be a Numerical Value. ")

            # Employee's Contract Date
            while True:
                try:
                    year = int(input("Enter Contract year: "))
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

            contract_date = str(year) + '-' + str(month) + '-' + str(day)

            # Employee's email
            while True:
                try:
                    email_duplicate = False
                    email = input("Enter Employee's Email: ")
                    cursor.execute("SELECT email FROM crud.employee")
                    email_rows = cursor.fetchall()
                    for row in email_rows:
                        if row[0] == email:
                            email_duplicate = True
                            break
                    if email.count("@") != 1:
                        print("Email must have only one @, Enter a Valid Email. ")
                    elif email.count(".com") != 1:
                        print("Email must have only one '.com', Enter a Valid Email. ")
                    elif email_duplicate:
                        print("Email already exists, Please enter another one.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            insert_employee = f"INSERT INTO `crud`.`employee` (`name`, `phone`, `address`, `ssn`, `contract_date`, `age`, `email`) VALUES ('{emp_name}', '{emp_phone}', '{emp_address}', '{emp_ssn}', '{contract_date}', '{age}', '{email}');"
            cursor.execute(insert_employee)
            conn.commit()

        # Viewing Employee's information
        case 2:
            print("=============================================================================================================================")
            print("'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'")
            show_all_data = "SELECT * FROM crud.employee"
            execute_query(show_all_data, cursor, conn)

        # Updating Employee's Information
        case 3:
            print("=============================================================================================================================")
            print("'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'")
            show_data_query = "SELECT * FROM crud.employee"
            execute_query(show_data_query, cursor, conn)

            while True:
                try:
                    cursor = conn.cursor()
                    id_exists = False
                    update_id = int(input("Enter The Employee's ID that Needed To be Updated: "))
                    cursor.execute("SELECT id FROM crud.employee; ")
                    employee_ids = cursor.fetchall()
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

            while True:
                while True:
                    try:
                        print("'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'")
                        cursor.execute(f"SELECT name, phone, address, ssn, contract_date, age, email FROM crud.employee WHERE (id= '{update_id}'); ")
                        old_data = cursor.fetchall()
                        print(old_data)
                        update_selection = int(input("To Update the Name enter -1- \n To Update the Phone Number enter -2- \n To Update the Address enter -3- \n To Update the SSN enter -4- \n To Update the Contract Date enter -5- \n To Update the Age enter -6- \n To Update the Email enter -7- \n To Update All of the Employee information enter -8- \n To Exit enter -0- \n Enter Your Selection : "))
                        if update_selection in (0,1, 2, 3, 4, 5, 6, 7, 8):
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid Input, Enter one of the Selection: ")

                match update_selection:
                        case 1:
                            cursor.execute(f"SELECT name FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_name = cursor.fetchall()
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
                            cursor.execute(f"UPDATE crud.employee SET name = '{new_name}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 2:
                            cursor.execute(f"SELECT phone FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_phone = cursor.fetchall()
                            print("The Old Phone Number is : ", old_phone)
                            while True:
                                try:
                                    phone_duplicate = False
                                    new_phone = input("Enter the new Employee's Phone : ")
                                    cursor.execute("SELECT phone FROM crud.employee;")
                                    phone_rows = cursor.fetchall()
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
                            cursor.execute(f"UPDATE crud.employee SET phone = '{new_phone}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 3:
                            cursor.execute(f"SELECT address FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_address = cursor.fetchall()
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

                                cursor.execute(f"UPDATE crud.employee SET address = '{new_address}' WHERE (id = '{update_id}')")
                                conn.commit()
                                break

                        case 4:
                            cursor.execute(f"SELECT ssn FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_ssn = cursor.fetchall()
                            print("The Old Social Security Number is : ", old_ssn)
                            while True:
                                try:
                                    ssn_duplicate = False
                                    new_ssn = input("Enter Employee's SSN : ")
                                    cursor.execute("SELECT ssn FROM crud.employee")
                                    ssn_rows = cursor.fetchall()
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

                            cursor.execute(f"UPDATE crud.employee SET ssn = '{new_ssn}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 5:
                            cursor.execute(f"SELECT contract_date FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_contract_date = cursor.fetchall()
                            print("The Old Contract-Date is : ", old_contract_date)
                            cursor.execute(f"SELECT age FROM crud.employee WHERE (id= '{update_id}'); ")
                            getAge = str(cursor.fetchall())
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
                            cursor.execute(f"UPDATE crud.employee SET contract_date = '{new_contract_date}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 6:
                            cursor.execute(f"SELECT age FROM crud.employee WHERE (id= '{update_id}'); ")
                            getAge = str(cursor.fetchall())
                            old_age = int(''.join([char for char in getAge if char.isdigit()]))
                            print("The Old age is : ", old_age)
                            cursor.execute(f"SELECT contract_date FROM crud.employee WHERE (id= '{update_id}'); ")
                            contract_date = str(cursor.fetchall())
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

                            cursor.execute(f"UPDATE crud.employee SET age = '{new_age}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 7:
                            cursor.execute(f"SELECT email FROM crud.employee WHERE (id= '{update_id}'); ")
                            old_email = cursor.fetchall()
                            print("The Old Email is : ", old_email)
                            while True:
                                try:
                                    email_duplicate = False
                                    new_email = input("Enter Employee's Email: ")
                                    cursor.execute("SELECT email FROM crud.employee")
                                    email_rows = cursor.fetchall()
                                    for row in email_rows:
                                        if row[0] == new_email:
                                            email_duplicate = True
                                            break
                                    if new_email.count("@") != 1:
                                        print("Email must have only one @, Enter a Valid Email. ")
                                    elif new_email.count(".com") != 1:
                                        print("Email must have only one -.com-, Enter a Valid Email. ")
                                    elif email_duplicate:
                                        print("Email already exists, Please enter another one.")
                                    else:
                                        break
                                except ValueError as e:
                                    print(e)

                            cursor.execute(f"UPDATE crud.employee SET email = '{new_email}' WHERE (id = '{update_id}')")
                            conn.commit()

                        case 8:
                            while True:
                                try:
                                    emp_name = input("Enter new Employee Name: ")
                                    numbers = [num for num in emp_name if num.isdigit()]
                                    if numbers:
                                        raise ValueError("Names cannot contain numbers. Enter a valid name: ")
                                    elif emp_name == " " or emp_name == "":
                                        print("Please enter a Name.")
                                    else:
                                        break
                                except ValueError as e:
                                    print(e)

                            while True:
                                try:
                                    phone_duplicate = False
                                    emp_phone = input("Enter new Employee's Phone : ")
                                    cursor.execute("SELECT phone FROM crud.employee;")
                                    phone_rows = cursor.fetchall()
                                    for row in phone_rows:
                                        if row[0] == emp_phone:
                                            phone_duplicate = True
                                            break
                                    if phone_duplicate:
                                        print("Phone Number already exists, Enter another one. ")
                                    elif len(emp_phone) != 11 or not emp_phone.isdigit():
                                        print("Phone Number Must be 11 numerical values: ")
                                    else:
                                        break
                                except ValueError as e:
                                    print(e)

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

                            emp_address = str(building_number) + building + ", " + street_name + ", " + city + ", " + country + "."

                            while True:
                                try:
                                    ssn_duplicate = False
                                    emp_ssn = input("Enter new Employee's SSN : ")
                                    cursor.execute("SELECT ssn FROM crud.employee")
                                    ssn_rows = cursor.fetchall()
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
                                    print("Invalid Social Security Number, Please enter a valid one.")

                            cursor.execute(f"SELECT age FROM crud.employee WHERE (id= '{update_id}'); ")
                            getAge = str(cursor.fetchall())
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

                            contract_date = str(year) + '-' + str(month) + '-' + str(day)

                            while True:
                                try:
                                    new_age = int(input("Enter new Employee's age: "))
                                    if new_age > 60 or new_age < 18:
                                        print("Invalid working age, enter an age between 18 and 60. ")
                                    elif (2023 - (year - 18)) > new_age:
                                        print(f"Invalid Age Employee must be at least '{2023 - (year - 18)}' to work at '{year}'. ")
                                    else:
                                        break
                                except ValueError:
                                    print("Age must be a Numerical Value. ")

                            cursor.execute(f"UPDATE crud.employee SET age = '{new_age}' WHERE (id = '{update_id}')")
                            conn.commit()

                            while True:
                                try:
                                    email_duplicate = False
                                    email = input("Enter new Employee's Email: ")
                                    cursor.execute("SELECT email FROM crud.employee")
                                    email_rows = cursor.fetchall()
                                    for row in email_rows:
                                        if row[0] == email:
                                            email_duplicate = True
                                            break
                                    if email.count("@") != 1:
                                        print("Email must have only one @, Enter a Valid Email. ")
                                    elif email.count(".com") != 1:
                                        print("Email must have only one -.com-, Enter a Valid Email. ")
                                    elif email_duplicate:
                                        print("Email already exists, Please enter another one.")
                                    else:
                                        break
                                except ValueError as e:
                                    print(e)

                            insert_employee = f"UPDATE `crud`.`employee` SET `name` = '{emp_name}', `phone` = '{emp_phone}', `address` = '{emp_address}', `ssn` = '{emp_ssn}', `contract_date` = '{contract_date}', `age` = '{age}', `email` = '{email}' WHERE (`id` = '{update_id}');"
                            cursor.execute(insert_employee)
                            conn.commit()
                        case 0:
                            break
                        case _:
                            print("Unexpected Error, Please Restart the application.")

        # Deleting an Employee Information
        case 4: 
            print("'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'")
            showData = "SELECT * FROM crud.employee"
            execute_query(showData, cursor, conn)
            while True:
                try:
                    cursor = conn.cursor()
                    idExists = False
                    deleteID = int(input("Enter The Employee's ID that Needed To be Deleted :"))
                    cursor.execute("SELECT id FROM crud.employee; ")
                    employeeIDs = cursor.fetchall()
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

            cursor.execute(f"SELECT * FROM crud.employee WHERE (id= '{deleteID}'); ")
            deleteInfo = cursor.fetchall()
            while True:
                try:
                    deleteConfirmation = input("Are you sure you want to delete:\n   'ID''Name'     'Phone'          'Address'                        'SSN'             'Contract Date'        'Age'       'Email'\n"
                                      f"{deleteInfo}\nEnter Your Selection (y/n): ")
                    if deleteConfirmation in ('y', 'n'):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid Input.")
            match deleteConfirmation:
                case 'y':
                    cursor.execute(f"DELETE FROM crud.employee WHERE (id = '{deleteID}')")
                    conn.commit()
                case 'n':
                    print("Back To the Main Menu.......")
                case _:
                    print("Unexpected Error, Please Restart the application")

        # Exiting from the Application
        case 5:
            print("Closing Application.......")
            break
        
        #Handling Unexpected match errors
        case _:
            print("Unexpected Error, Please Restart the application")

# Close the cursor and the database connection.
cursor.close()
conn.close()