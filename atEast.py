
# Global Variable
user = {}
appointments = {}
id = 1

# Sign Up ^^
def signUp():
    print("\n====================")
    print("   ^^ SIGN UP ^^    ")
    print("====================")
    username = input("Enter a username: ")
    print("====================")
    password = input("Enter a password: ")
    print("====================")
    user[username] = password
    print("Sign up successfully")
    print("====================")    
    return

# Sign In ^^
def signIn():
    while True:
        print("\n====================")
        print("   ^^ SIGN IN ^^    ")
        print("====================")
        username = input("Enter a username: ")
        print("====================")
        password = input("Enter a password: ")
        print("====================")

        if username == "admin" and password == "1234":
            print("Logging in as ADMIN...")
            print("====================")
            adminDashboard()
            return
        elif username not in user:
            print("User not found!")
            print("====================")
            break
        elif user[username] == password:
            print(f"Login Successfully as {username}")
            print("====================")
            userDashboard(username)
            return
        else:
            print("Incorrect Password")
            print("====================")

# User Dashboard ^^
def userDashboard(username):
    while True:
        print("\n====================")
        print(f" ^^ Welcome {username} ^^")
        print("====================")
        print("1. Book Appointment\n2. Check Appointment\n3. Cancel Appointment\n4. Logout")
        print("====================")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                bookAppointment(username)
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                break
            else:
                print("Invalid Choice!")
        except ValueError:
            print("Only numbers should be type!")

# Admin Dashboard ^^
def adminDashboard():
    while True:
        print("====================")
        print("1. Check Appointment\n2. logout")
        print("====================")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            if not appointments:
                print("No appointments yet")
                continue

            for appointment in appointments.values():
                print(f"{appointment['id']}. {appointment['lastName']}, {appointment['firstName']}, {appointment['middleName']}")
            
            
            IDsearch = int(input("Enter ID number to view details: "))
            
            for appointmentData in appointments.values():
                if appointmentData['id'] == IDsearch:
                    print(f"FULL NAME: {appointmentData['firstName']} {appointmentData['middleName']} {appointmentData['lastName']}")
                    print(f"AGE: {appointmentData['age']}")
                    print(f"SEX: {appointmentData['sex']}")
                    print(f"ADDRESS: {appointmentData['address']}")
                    print(f"MOBILE #: {appointmentData['mobileNum']}")
                    print(f"CONCERN: {appointmentData['concern']}")
                    print(f"AGE: {appointmentData['age']}")
                    break
            else:
                print("Id not found")

        elif choice == 2:
            break

# Book Appointment ^^          
def bookAppointment(username):
    global id
    if username in appointments:
        print("You have book an appointment already: ")
        return

    print("====================")
    print("  APPOINTMENT FORM  ")
    print("====================")
    firstName = input("Enter your first name: ")
    print("====================")
    lastName = input("Enter your last name: ")
    print("====================")
    middleName = input("Enter your middle name: ")
    print("====================")
    age = int(input("Enter your age name: "))
    print("====================")
    sex = input("Enter your sex (female or male): ")
    print("====================")
    address = input("Enter your address: ")
    print("====================")
    mobileNum = int(input("Enter your mobile #: "))
    print("====================")
    concern = input("Enter your concern: ")
    print("====================")

    appointments[username] = {
        "id": id,
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "age": age,
        "sex": sex,
        "address": address,
        "mobileNum": mobileNum,
        "concern": concern
    }

    print(f"Appointment booked successfully: Your ID is {id} ")
    id += 1
    print("====================")


# Main Function
while True:
    print("\n====================")
    print("1. SignUp\n2. SignIn\n3. Exit")
    print("====================")

    try:
        choice = int(input("Enter your choice: "))
        print("====================")

        if choice == 1:
            signUp()
        elif choice == 2:
            signIn()
        elif choice == 3:
            break
        else:
            print("Invalid Choice!")
    
    except ValueError:
        print("Only numbers should be type!")



