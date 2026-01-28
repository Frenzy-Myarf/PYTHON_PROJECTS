import time
# Global Variable
user = {}
appointments = {}
id = 1



# Sign Up ^^
def signUp():
    print("\n"+"=" * 50)
    print("^^ SIGN UP ^^".center(50))
    print("=" * 50)
    username = input("Enter a username: ")
    print("=" * 50)
    password = input("Enter a password: ")
    print("=" * 50)
    user[username] = password
    print(f"Sign up successfully ^^ as (•‿•) {username}")
    print("=" * 50)    
    return

# Sign In ^^
def signIn():
    while True:
        print("\n" + "=" * 50)
        print("^^ SIGN IN ^^".center(50))
        print("=" * 50)
        username = input("Enter a username: ")
        print("=" * 50)
        password = input("Enter a password: ")
        print("=" * 50)

        if username == "admin" and password == "1234":
            print("Logging in as ADMIN...")
            print("=" * 50)
            adminDashboard()
            return
        elif username not in user:
            print("User not found!")
            print("=" * 50)
            break
        elif user[username] == password:
            print(f"Login Successfully ^^ as {username}")
            print("=" * 50)
            userDashboard(username)
            return
        else:
            print("Incorrect Password ^^")
            print("=" * 50)

# User Dashboard ^^
def userDashboard(username):
    while True:
        print("\n" + "=" * 50)
        print(f"^^ Welcome (•‿•) {username} ^^".center(50))
        print("=" * 50)
        print("1. Book Appointment".center(50))
        print("2. Check Appointment".center(50))
        print("3. Cancel Appointment".center(52))
        print("4. Logout".center(40))
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice: "))
            print("=" * 50)
            if choice == 1:
                bookAppointment(username)
            elif choice == 2:
                print("\n" + "=" * 50)
                print("^^ Check Appointment ^^".center(50))
                print("=" * 50)
                if username not in appointments:
                    print("\n" + "=" * 50)
                    print("No appointments yet! ^^".center(50))
                    print("=" * 50)
                
                
                IDSearch = int(input("Enter id # to view details: "))
                print("=" * 50)

                appointment = appointments[username]
      
                if appointment['id'] != IDSearch:
                    print("\n" + "=" * 50)
                    print("^^ this appointment is not yours!".center(50))
                    print("=" * 50)
                    continue

                print("\n" + "-" * 50)
                print(f"STATUS: {appointment['status']}")
                print(f"FULL NAME: {appointment['firstName']} {appointment['middleName']} {appointment['lastName']}")
                print(f"AGE: {appointment['age']}")
                print(f"SEX: {appointment['sex']}")
                print(f"ADDRESS: {appointment['address']}")
                print(f"CONCERN: {appointment['concern']}")
                print(f"MOBILE #: {appointment['mobileNum']}")
                print("-" * 50)

                if appointment['status'] == "rejected":
                    print("\n" + "-" * 50)
                    print("1. Delete Appointment".center(50))
                    print("2. Back".center(36))
                                    
                    action = int(input("Enter action: "))

                    if action == 1:
                        del appointments[appointment]
                        print("\n" + "-" * 50)
                        print("Appointment deleted successfully (=^.^=)")
                        print("-" * 50)
                        return

            elif choice == 3:
                print("\n" + "=" * 50)
                print("^^ Cancel Appointment ^^".center(50))
                print("=" * 50)
                if username not in appointments:
                    print("\n" + "=" * 50)
                    print("No appointments yet! ^^".center(50))
                    print("=" * 50)
                
                IDSearch = int(input("Enter your Appointment ID to cancel ^^: "))
                print("=" * 50)

                appointment = appointments[username]

                if appointment['id'] != IDSearch:
                    print("\n" + "=" * 50)
                    print("The appointment ID you have input is not yours! ^^")
                    print("=" * 50)
                    continue

                if appointment['status'] == "accepted":
                    print("\n" + "=" * 50)
                    print("Cannot be cancelled once accepted! ^^")
                    print("=" * 50)
                    continue
                
                del appointments[username]
                print("\n" + "=" * 50)
                print("Appointment deleted successfully (=^.^=)")
                print("=" * 50)
                
                
            elif choice == 4:
                print("\n" + "=" * 50)
                time.sleep(1)
                print("Logging out...")
                time.sleep(3)
                print("=" * 50)
                break
            else:
                print("Invalid Choice! (=^.^=)")
                print("=" * 50)
        except ValueError:
            print("Only numbers should be type! (=^.^=)")
            print("=" * 50)

# Admin Dashboard ^^
def adminDashboard():
    while True:
        print("\n"+"=" * 50)
        print("^^ Welcome Admin ^^".center(50))
        print("=" * 50)
        print("1. Check Appointment".center(50))
        print("2. logout".center(40))
        print("=" * 50)

        choice = int(input("Enter your choice: "))
        print("=" * 50)
        if choice == 1:
            if not appointments:
                print("\nNo appointments yet ^^")
                continue

            for appointment in appointments.values():
                if appointment['status'] != "rejected":
                    print("-" * 50)
                    print(f"{appointment['id']}. {appointment['lastName']}, {appointment['firstName']}, {appointment['middleName']} - > {appointment['status']}")
                
            
            IDsearch = int(input("Enter ID number to view details: "))
            print("=" * 50)
            
            for appointmentData in appointments.values():
                #if appointmentData['status'] == "rejected":
                    #print("Its been rejected") 
                if appointmentData['id'] == IDsearch and appointment['status'] == "pending":
                    print("-" * 50)
                    print(f"STATUS: {appointmentData['status']}")
                    print(f"FULL NAME: {appointmentData['firstName']} {appointmentData['middleName']} {appointmentData['lastName']}")
                    print(f"AGE: {appointmentData['age']}")
                    print(f"SEX: {appointmentData['sex']}")
                    print(f"ADDRESS: {appointmentData['address']}")
                    print(f"MOBILE #: {appointmentData['mobileNum']}")
                    print(f"CONCERN: {appointmentData['concern']}")
                    print("-" * 50)
                    
                    print("=" * 50)
                    print("1. accept".center(50))
                    print("2. reject".center(50))
                    print("=" * 50)
                    
                    action = int(input("Enter action (1 or 2): "))
                    print("=" * 50)
                    if action == 1:
                        appointmentData.update({"status": "accepted"})
                    elif action == 2:
                        appointmentData.update({"status": "rejected"})
                    else:
                        print("Invalid action! (=^.^=)")
                elif appointmentData['id'] == IDsearch and appointment['status'] == "accepted":
                    print("-" * 50)
                    print(f"STATUS: {appointmentData['status']}")
                    print(f"FULL NAME: {appointmentData['firstName']} {appointmentData['middleName']} {appointmentData['lastName']}")
                    print(f"AGE: {appointmentData['age']}")
                    print(f"SEX: {appointmentData['sex']}")
                    print(f"ADDRESS: {appointmentData['address']}")
                    print(f"MOBILE #: {appointmentData['mobileNum']}")
                    print(f"CONCERN: {appointmentData['concern']}")
                    print("-" * 50)
                    
                    print("\n" + "=" * 50)
                    print("1. Mark As Done".center(50))
                    print("2. Leave it be".center(50))
                    print("=" * 50)

                    action = int(input("Enter action: "))
                    print("=" * 50)

                    if action == 1:
                        del appointments[appointmentData]
                        print("Mark as done successfully ^^")
                        break
                    elif action == 2:
                        continue

                    
                else:
                    print("Id not found! (=^.^=)")
                    print("=" * 50)

        elif choice == 2:
            print("\n" + "=" * 50)
            time.sleep(1)
            print("Logging out...")
            time.sleep(3)
            print("=" * 50)
            break

# Book Appointment ^^          
def bookAppointment(username):
    global id
    if username in appointments:
        print("You have book an appointment already: ")
        return

    print("\n"+"=" * 50)
    print(" ^^ APPOINTMENT FORM ^^".center(50))
    print("=" * 50)
    firstName = input("Enter your first name: ").upper()
    print("=" * 50)
    lastName = input("Enter your last name: ").upper()
    print("=" * 50)
    middleName = input("Enter your middle name: ").upper()
    print("=" * 50)
    while True:
        age = int(input("Enter your age: "))
        if age < 0:
            print("\n" + "=" * 50)
            print("Age can't be negative number ^^")
            print("=" * 50)
        elif age >= 0 and age < 18:
            print("\n" + "=" * 50)
            print("not adult yet ^^")
            print("=" * 50)
        elif age >= 18 and age <= 110:
            break
        else:
            print("\n" + "=" * 50)
            print("What are you a gueness record holder bruh ^^")
            print("=" * 50) 
    print("=" * 50)
    while True:
        sex = input("Enter your sex (female or male): ").capitalize()
        if sex == "Male" or sex == "Female":
            break
        else:
            print("Only male and female is accepted bruh ^^")
    print("=" * 50)
    address = input("Enter your address: ").capitalize()
    print("=" * 50)
    mobileNum = input("Enter your mobile #: ")
    print("=" * 50)
    concern = input("Enter your concern: ").capitalize()
    print("=" * 50)

    appointments[username] = {
        "id": id,
        "status": "pending",
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "age": age,
        "sex": sex,
        "address": address,
        "mobileNum": mobileNum,
        "concern": concern
    }

    print("\n"+"=" * 50)
    print(f"Appointment booked successfully: Your ID is {id} ")
    id += 1
    print("=" * 50)


# Main Function
while True:
    print("\n" + "=" * 50)
    print("1. SignUp".center(50))
    print("2. SignIn".center(50))
    print("3. Exit".center(48))
    print("=" * 50)

    try:
        choice = int(input("Enter your choice: "))
        print("=" * 50)

        if choice == 1:
            signUp()
        elif choice == 2:
            signIn()
        elif choice == 3:
            print("\n" + "=" * 50)
            time.sleep(1)
            print("Exiting program...")
            time.sleep(3)
            print("=" * 50)
            break
        else:
            print("Invalid Choice! (=^.^=)")
            print("=" * 50)
    
    except ValueError:
        print("\n" + "=" * 50)
        print("Only numbers should be type!")
        print("=" * 50)

