#This is my employee database project

from enum import Enum

class Employees:

    number_of_emps = 0
    all_employees = {}
    DEFAULT_RAISE_AMOUNT = 5
    DEFAULT_PAY = 50000
    def __init__(self, first, last, email, number, pay=DEFAULT_PAY):
        self.first = first
        self.last = last
        self.email = email
        self.number = number
        self.pay = pay
        Employees.number_of_emps += 1
        self.emp_id = Employees.number_of_emps
        Employees.all_employees[self.emp_id] = self


    def display():
        for emp_id, emp in Employees.all_employees.items():
            print(f"ID: {emp_id},  Name: {emp.first} {emp.last}, Email: {emp.email}, Phone: {emp.number}, Pay: {emp.pay}")

    def find(search):
        if len(search) == 2:
            first = search[0].capitalize()
            last = search[1].capitalize()
            check_status = 0
            for emp_id, emp in Employees.all_employees.items():
                if first == emp.first and last == emp.last:
                    print(f"ID: {emp_id},  Name: {emp.first} {emp.last}, Email: {emp.email}, Phone: {emp.number}, Pay: {emp.pay}")
                    check_status = 1
            if check_status == 0:
                print ("The entered employee could not be found")
        elif len(search) == 1:
            try:
                id = int(search[0])
                for emp_id, emp in Employees.all_employees.items():
                    if emp_id == id:
                        print(f"ID: {emp_id},  Name: {emp.first} {emp.last}, Email: {emp.email}, Phone: {emp.number}, Pay: {emp.pay}")
                        return
                print ("The entered employee could not be found")
            except:
                query = search[0].capitalize()
                check_status = 0
                for emp_id, emp in Employees.all_employees.items():
                    if query == emp.first:
                        print(f"ID: {emp_id},  Name: {emp.first} {emp.last}, Email: {emp.email}, Phone: {emp.number}, Pay: {emp.pay}")
                        check_status = 1
                    elif query == emp.last:
                        print(f"ID: {emp_id},  Name: {emp.first} {emp.last}, Email: {emp.email}, Phone: {emp.number}, Pay: {emp.pay}")
                        check_status = 1
                if check_status == 0:
                    print ("The entered employee could not be found")
        else:
            print("Error with usage of FIND command\nType \"Find\" to access the help page")
        

    
    def remove(id):

        if id in Employees.all_employees:
            for emp_id, emp in Employees.all_employees.items():
                if id == emp_id:
                    first = emp.first
                    last = emp.last
                    break
            confirmation = input(f"Type \"Confirm\" to confirm that you would like to remove {first} {last} from Employee Database\n> ").upper()
            if confirmation == "CONFIRM":
                del Employees.all_employees[emp_id]
                Employees.number_of_emps -= 1
                print(f"{first} {last} has been removed from the Employee Database")
                return
        else:
            print("The entered ID could not be found")
        

    def apply_raise(self, raise_amount = DEFAULT_RAISE_AMOUNT):
        raise_amount /= 100
        raise_amount += 1
        pay = self.pay * raise_amount
        self.pay = round(pay,2)

    def sort(input):
        value = input[0]
        order = input[1]
        if order == "DESC":
            order = True
        elif order == "ASC":
            order = False
        else:
            print("Error with order for some reason")

        if value == "NAME":
            sorted_employees = dict(sorted(Employees.all_employees.items(), key= lambda emp: emp[1].last + ' ' + emp[1].first, reverse= order))
        elif value == "PAY":
            sorted_employees = dict(sorted(Employees.all_employees.items(), key= lambda emp: emp[1].pay, reverse= order))
        elif value == "ID":
            sorted_employees = dict(sorted(Employees.all_employees.items(), key= lambda emp: emp[0], reverse= order))
        else:
            print("Error with the Value for some reason")
        
        print("The Database has been sorted")
        Employees.all_employees = sorted_employees

    def emp_count():
        return Employees.number_of_emps
    

class Options(Enum):
    ADD = 'ADD'
    REMOVE = 'REMOVE'
    FIND = 'FIND'
    DISPLAY = 'DISPLAY'
    APPLY_RAISE = 'RAISE'
    COUNT = 'COUNT'
    SORT = 'SORT'

class Help:
    
    help_sections = {
         Options.ADD: """
        Syntax: ADD first surname email number [pay]

            Description:
                Adds a new employee to the database with the provided details.
                The `pay` argument is optional and will default to {} if not specified.

            Arguments:
                first       (Required) The first name of the employee.
                surname     (Required) The surname of the employee.
                email       (Required) The email address of the employee.
                number      (Required) The contact number of the employee.
                pay         (Optional) The starting salary of the employee, must be an integer or float.

            Examples:
                ADD John Doe john.doe@example.com 5551234
                ADD Alice Smith alice.smith@example.com 5555678 60000



        """,
        Options.REMOVE: """
        Syntax: REMOVE emp_id

            Description:
                Removes an employee from the database. This action cannot be undone 
                once confirmed.

            Arguments:
                emp_id      (Required) The unique ID of the employee to be removed. 
                            Must be an integer and a valid ID within the database.

            Examples:
                REMOVE 123







        """,
        Options.FIND: """
        Syntax: FIND emp_id | first | surname | first surname

            Description:
                Searches for an employee in the database and displays their information.
                You can search using the employee ID, first name, last name, or a 
                combination of first and last names.

            Arguments:
                emp_id      (Optional) The unique ID of the employee, must be an integer.
                first       (Optional) The first name of the employee.
                surname     (Optional) The surname of the employee.
                first surname
                            (Optional) A combination of first and last name for the search.

            Examples:
                FIND 123
                FIND John
                FIND Doe
                FIND John Doe
        """,
        Options.APPLY_RAISE: """
        Syntax: RAISE all | emp_id [raise_amount]

            Description:
                Gives a raise to a specific employee or to all employees. 
                If the second argument is omitted, a default raise amount is applied.
                Current default raise amount is {}%

            Arguments:
                all         (Required if used) Applies the raise to all employees.
                emp_id      (Required if used) The unique ID of the employee to receive the raise.
                            Must be an integer and a valid ID within the database.
                raise_amount
                            (Optional) The percentage increase to the employee's pay. 
                            Must be an integer.

            Examples:
                RAISE all
                RAISE 123
                RAISE 123 10
        """,
        Options.SORT: """
        Syntax: SORT Name Order | Pay Order

            Description:
                Sorts the Employee database based on pay or name and either by ascending or descending order.

            Arguments:
                Name         (Required if used) This sorts the database by name.
                Pay      (Required if used) This sorts the database by Pay
                Order      (Required if used) This sorts the database in either Ascending or Descending order
            Examples:
                SORT Pay asc
                SORT name Desc
                SORT PAY DESC
                SORT name asc


"""

    }
    def myHelp(command):
        if command == Options.ADD.value:
            default_wage = Employees.DEFAULT_PAY
            print(Help.help_sections[Options.ADD].format(default_wage))
        elif command == Options.REMOVE.value:
            print(Help.help_sections[Options.REMOVE])
        elif command == Options.FIND.value:
            print(Help.help_sections[Options.FIND])
        elif command == Options.APPLY_RAISE.value:
            default_raise = Employees.DEFAULT_RAISE_AMOUNT
            print(Help.help_sections[Options.APPLY_RAISE].format(default_raise))
        elif command == Options.SORT.value:
            print(Help.help_sections[Options.SORT])
        elif command == "HELP":
            print("""
            _______Help Menu_______
                


                Please enter one of the inputs below:


                add
                
                remove
                
                find
                
                display
                
                raise
                
                count
                
                Sort

            """)
        else:
            command = command.lower()
            print (f" \'{command}\' is not a recognised command\nUse the \"Help\" command to see list of commands\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
emp_1 = Employees('Bukunmi', 'Alexander', 'Bukunmiodejay@gmail.com', "07546579549", 84934.0)
emp_2 = Employees('John', 'Doe', 'JohnDoe@gmail.com', "0753242354356")
emp_11 = Employees('Bukunmi', 'John', 'bukunmi.john@gmail.com', '07456789123', 75000.0)
emp_3 = Employees('Bukunmi', 'Okafor', 'bukunmi.okafor@yahoo.com', '07911223344', 80500.0)
emp_4 = Employees('Ada', 'Alexander', 'ada.alexander@gmail.com', '07345678901', 72000.0)
emp_5 = Employees('Tomiwa', 'Alexander', 'tomiwa.alex@gmail.com', '07899887766')
emp_6 = Employees('Chinedu', 'Obi', 'chinedu.obi@gmail.com', '07112233445', 69000.0)
emp_7 = Employees('Amaka', 'Uche', 'amaka.uche@gmail.com', '07099887755', 71000.0)
emp_8 = Employees('John', 'Boyega', 'John.Boyega@gmail.com', '07223344556')
emp_9 = Employees('Tomiwa', 'Adetayo', 'tomiwa.adetayo@gmail.com', '07999887711', 76000.0)
emp_10 = Employees('Chioma', 'John', 'chioma.john@gmail.com', '07012345678')

print("Welcome to Bukunmi's Employee Database Prototype\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while True:
    action = input("What would you like to do?\n> ").upper()
    parameters = action.split()
    if parameters == []:
        continue
    command = parameters[0]

    if command == Options.DISPLAY.value:
            Employees.display()
    
    elif command == Options.COUNT.value:
            count = Employees.emp_count()
            print(f"\tThe number of current employees is: {count}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    elif len(parameters) == 1:
        Help.myHelp(command)

    elif len(parameters) > 1:
        if command == Options.ADD.value:
            if len(parameters) != 5:
                if len(parameters) == 6:
                    first = parameters[1].capitalize()
                    last = parameters[2].capitalize()
                    email = parameters[3].lower()
                    number = parameters[4]
                    pay = parameters[5]
                    try:
                        pay = float(pay)
                        confirmation = input(f"\tDetails:\n\t\tFirst: \"{first}\",\n\t\tLast: \"{last}\",\n\t\tEmail: \"{email}\",\n\t\tNumber: \"{number}\",\n\t\tPay: \"{pay}\"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                        if confirmation == "CONFIRM":
                            Employees(first,last, email, number, pay), 
                            print(f"{first} {last} has been added to the Employee Database\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        else:
                            print("Please use command again")
                            print("EXIT_SUCCESS")
                    except:
                        print("Please enter a number for pay")
                        continue
                        
                    
                else:    
                    print("Error with usage of ADD command\nType \"Add\" to access the help page")
                    continue
            else:
                first = parameters[1].capitalize()
                last = parameters[2].capitalize()
                email = parameters[3].lower()
                number = parameters[4]
                confirmation = input(f"First: \"{first}\", Last: \"{last}\", Email: \"{email}\", Number: \"{number}\", Pay: \"50000\"\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                if confirmation == "CONFIRM":
                    Employees(first, last, email, number)
                    print(f"\t{first} {last} has been added to the Employee Database")
                else:
                    print("Please use command again")              

            

            
            

        elif command == Options.REMOVE.value:
            err = "Error with usage of REMOVE command\nType \"Remove\" to access the help page"
            if len(parameters) != 2:
                print(err)
                continue
            else:
                try:
                    id = int(parameters[1])
                    Employees.remove(id)

                except:
                    print(err)
                    


        elif command == Options.FIND.value:
            parameters.pop(0)
            Employees.find(parameters)




        elif command == Options.APPLY_RAISE.value:
            err = "Error with usage of RAISE command\nType \"Raise\" to access the help page"
            parameters.pop(0)
            args = len(parameters)
            if args <=2:
                try:
                    id = int(parameters[0])
                    for emp_id, emp in Employees.all_employees.items():
                        if id == emp_id:
                            first = emp.first
                            last = emp.last
                            pay = emp.pay
                            ext = "Raise has successfully been applied to {}{}\nNew pay is {}"
                            if args == 2:
                                try:
                                    raise_amount = int(parameters[1])
                                    confirmation = input(f"Raise ID: {emp_id}, {first} {last}'s pay ({pay}) by {raise_amount}%\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                                    if confirmation == "CONFIRM":
                                        emp.apply_raise(raise_amount)
                                        pay = emp.pay
                                        print(ext.format(first, last, pay))
                                    else:
                                        print("Please use command again")
                                except:
                                    print(err)
                            else:
                                raise_amount = Employees.DEFAULT_RAISE_AMOUNT
                                confirmation = input(f"Raise ID: {emp_id}, {first} {last}'s pay ({pay}) by {raise_amount}%\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                                if confirmation == "CONFIRM":
                                    emp.apply_raise()
                                    pay = emp.pay
                                    print(ext.format(first, last, pay))
                                else:
                                    print("Please use command again")
                except:
                    if parameters[0] == "ALL":
                        ext = "Raise has successfully been applied to all Employees\nType \"Display\" to see the updated pays"
                        if args == 2:
                            try:
                                raise_amount = int(parameters[1])
                                confirmation = input(f"Raise all Employees's pay by {raise_amount}%\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                                if confirmation == "CONFIRM":
                                    for emp_id, emp in Employees.all_employees.items():
                                        emp.apply_raise(raise_amount)
                                    print(ext)
                                else:
                                    print("Please use command again")
                            except:
                                print(err)
                        else:
                            raise_amount = Employees.DEFAULT_RAISE_AMOUNT
                            confirmation = input(f"Raise all Employees's pay by {raise_amount}%\nType \"Confirm\" below to confirm the information is correct\n> ").upper()
                            if confirmation == "CONFIRM":
                                for emp_id, emp in Employees.all_employees.items():
                                    emp.apply_raise()
                                    print(ext)
                            else:
                                print("Please use command again")
                    else:
                        print(err)
        elif command == Options.SORT.value:
            parameters.pop(0)
            Employees.sort(parameters)
        else:
            action = action.lower()
            print (f" {action} is not a recognised command\nUse the \"Help\" command to see list of commands")
            



