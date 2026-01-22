user = {}
appointments = {}

def signUp():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user[username] = password
    print("Sign up successfully")
    return

def signIn():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username == "admin" and password == "1234":
            print("Logging in as ADMIN...")
            adminDashboard()
        elif username not in user:
            print("User not found!")
        elif user[username] == password:
            print(f"Login Successfully as {username}")
            userDashboard(username)
        else:
            print("Incorrect Password")

def userDashboard(username):
    while True:
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

def adminDashboard():
    print("====================")
    print("1. Check Appointment\n2. logout")

def bookAppointment(username):
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
    address = input("Enter your address: ")
    print("====================")
    mobileNum = int(input("Enter your mobile #: "))
    print("====================")
    concern = input("Enter your concern: ")
    print("====================")

    appointments[username] = {
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "age": age,
        "address": address,
        "mobileNum": mobileNum,
        "concern": concern
    }

    print("Appointment booked successfully: ")



while True:
    print("====================")
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



