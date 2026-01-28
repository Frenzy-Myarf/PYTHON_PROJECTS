import time
from atEastSupabase import supabase


# Global Variable
#user = {}
#appointments = {}
#id = 1



# Sign Up ^^
def signUp():
    print("\n"+"=" * 50)
    print("^^ SIGN UP ^^".center(50))
    print("=" * 50)
    username = input("Enter a username: ")
    print("=" * 50)
    password = input("Enter a password: ")
    print("=" * 50)

    existingUser = supabase.table("users") \
        .select("*") \
        .eq("username", username) \
        .execute()
    
    if existingUser.data:
        print("\n" + "=" * 50)
        print("Username already exist! ^^".center(50))
        print("=" * 50)
        return
    
    
    supabase.table("users").insert({
        "username": username, 
        "password": password
    }).execute()
    print("\n" + "=" * 50)
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
        
        validUser = supabase.table("users") \
            .select("*") \
            .eq("username", username) \
            .execute()
        
        if not validUser.data:
            print("\n" + "=" * 50)
            print("User not found! ^^")
            print("=" * 50)
            return
        
        if validUser.data[0]["password"] == password:
            print("\n" + "=" * 50)
            time.sleep(1)
            print(f"^^ Logging in as {username} (•‿•)")
            time.sleep(3)
            print("=" * 50)
            userDashboard(username)
            return
        else:
            print("Incorrect password! ^^")

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
                
                IDSearch = int(input("Enter id # to view details: "))
                print("=" * 50)

                appointmentById = supabase.table("appointments") \
                .select("*") \
                .eq("id", IDSearch) \
                .execute()

                if not appointmentById.data:
                    print("\n" + "=" * 50)
                    print("Appointment ID does not exist.")
                    print("=" * 50)
                    continue
        
                
                appointment = appointmentById.data[0]
                
      
                if appointment['username'] != username:
                    print("\n" + "=" * 50)
                    print("^^ this appointment is not yours!".center(50))
                    print("=" * 50)
                    continue

                print("\n" + "-" * 50)
                print(f"STATUS: {appointment['status']}")
                print(f"FULL NAME: {appointment['firstname']} {appointment['middlename']} {appointment['lastname']}")
                print(f"AGE: {appointment['age']}")
                print(f"SEX: {appointment['sex']}")
                print(f"ADDRESS: {appointment['address']}")
                print(f"CONCERN: {appointment['concern']}")
                print(f"MOBILE #: {appointment['mobilenum']}")
                print("-" * 50)

                if appointment['status'] == "rejected":
                    print("\n" + "-" * 50)
                    print("1. Delete Appointment".center(50))
                    print("2. Back".center(36))
                                    
                    action = int(input("Enter action: "))

                    if action == 1:
                        #del appointments[appointment]
                        supabase.table("appointments") \
                        .delete() \
                        .eq("id", IDSearch) \
                        .eq("username", username) \
                        .execute()

                        print("\n" + "-" * 50)
                        print("Appointment deleted successfully (=^.^=)")
                        print("-" * 50)
                    else:
                        return

            elif choice == 3:
                print("\n" + "=" * 50)
                print("^^ Cancel Appointment ^^".center(50))
                print("=" * 50)
                #if username not in appointments:
                #    print("\n" + "=" * 50)
                #    print("No appointments yet! ^^".center(50))
                #    print("=" * 50)
                
                IDSearch = int(input("Enter your Appointment ID to cancel ^^: "))
                print("=" * 50)
                
                appointmentById = supabase.table("appointments") \
                    .select("*") \
                    .eq("id", IDSearch) \
                    .execute()
                
                if not appointmentById.data:
                    print("\n" + "=" * 50)
                    print("Sadly you have no appointments yet ^^")
                    print("=" * 50)
                    continue
                
                
                appointment = appointmentById.data[0]


                if appointment['username'] != username:
                    print("\n" + "=" * 50)
                    print("The appointment ID you have input is not yours! ^^")
                    print("=" * 50)
                    continue

                if appointment['status'] == "accepted":
                    print("\n" + "=" * 50)
                    print("Cannot be cancelled once accepted! ^^")
                    print("=" * 50)
                    continue
                
                if appointment['status'] == "rejected":
                    print("\n" + "=" * 50)
                    print("Your appointment is already been rejected (=^.^=) delete it instead")
                    print("=" * 50)
                    
                    action = int(input("Enter action: "))

                    if action == 1:
                        supabase.table("appointments") \
                        .delete() \
                        .eq("id", IDSearch) \
                        .eq("username", username) \
                        .execute()

                        print("\n" + "-" * 50)
                        print("Appointment deleted successfully (=^.^=)")
                        print("-" * 50)
                    else:
                        return
                
                supabase.table("appointments") \
                        .delete() \
                        .eq("id", IDSearch) \
                        .execute()

                print("\n" + "=" * 50)
                print("Appointment cancelled successfully (=^.^=)")
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

# Update Status shortcut
def updateStatus(appointmentID, newStatus):
    supabase.table("appointments") \
    .update({"status": newStatus}) \
    .eq("id", appointmentID) \
    .execute()

    print("=" * 50)
    print(f"Appointment {appointmentID} has been updated to {newStatus}")

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
            print("\n" + "=" * 50)
            print("^^ Check Appointment ^^".center(50))
            print("=" * 50)

            adminView = supabase.table("appointments") \
                .select("*") \
                .in_("status", ["pending", "accepted"]) \
                .order("id") \
                .execute()
            
            if not adminView or not adminView.data:
                print("\nNo appointments yet ^^")
                continue
            
            
            for appointment in adminView.data:
                if appointment['status'] != "rejected":
                    print("-" * 50)
                    print(f"{appointment['id']}. {appointment['lastname']}, {appointment['firstname']}, {appointment['middlename']} - > {appointment['status']}")
                
            
            IDsearch = int(input("Enter ID number to view details: "))
            print("=" * 50)
            
            adminIdSearch = supabase.table("appointments") \
                .select("*") \
                .eq("id", IDsearch) \
                .execute()
            
            if not adminIdSearch or not adminIdSearch.data:
                print("\n" + "=" * 50)
                print("Appointment not found! ^^".center(50))
                print("=" * 50)
                return
            
            appointmentData = adminIdSearch.data[0]

            print("\n" + "-" * 50)
            print(f"STATUS: {appointmentData['status']}")
            print(f"FULL NAME: {appointmentData['firstname']} {appointmentData['middlename']} {appointmentData['lastname']}")
            print(f"AGE: {appointmentData['age']}")
            print(f"SEX: {appointmentData['sex']}")
            print(f"ADDRESS: {appointmentData['address']}")
            print(f"MOBILE #: {appointmentData['mobilenum']}")
            print(f"CONCERN: {appointmentData['concern']}")
            print("-" * 50)
                    
            if appointmentData['status'] == "pending":
                print("\n" + "=" * 50)
                print("1. accept".center(50))
                print("2. reject".center(50))
                print("=" * 50)
                    
                action = int(input("Enter action (1 or 2): "))
                print("=" * 50)
                if action == 1:
                        updateStatus(IDsearch, "accepted")
                elif action == 2:
                        updateStatus(IDsearch, "rejected")
                else:
                        print("Invalid action! (=^.^=)")
            elif appointmentData['status'] == "accepted":
                    print("-" * 50)
                    print(f"STATUS: {appointmentData['status']}")
                    print(f"FULL NAME: {appointmentData['firstname']} {appointmentData['middlename']} {appointmentData['lastname']}")
                    print(f"AGE: {appointmentData['age']}")
                    print(f"SEX: {appointmentData['sex']}")
                    print(f"ADDRESS: {appointmentData['address']}")
                    print(f"MOBILE #: {appointmentData['mobilenum']}")
                    print(f"CONCERN: {appointmentData['concern']}")
                    print("-" * 50)
                    
                    print("\n" + "=" * 50)
                    print("1. Mark As Done".center(50))
                    print("2. Leave it be".center(50))
                    print("=" * 50)

                    action = int(input("Enter action: "))
                    print("=" * 50)

                    if action == 1:
                        supabase.table("appointments") \
                        .delete() \
                        .eq("id", IDsearch) \
                        .execute()

                        print(f"Appointment {IDsearch} been mark as done successfully ^^")



                    elif action == 2:
                        continue

                    
                #else:
                #    print("Id not found! (=^.^=)")
                #    print("=" * 50)

        elif choice == 2:
            print("\n" + "=" * 50)
            time.sleep(1)
            print("Logging out...")
            time.sleep(3)
            print("=" * 50)
            break

# Book Appointment ^^          
def bookAppointment(username):
    #global id
    #if username in appointments:
    #    print("You have book an appointment already: ")
    #    return

    existing = supabase.table("appointments") \
    .select("id") \
    .eq("username", username) \
    .execute()

    if existing.data:
        print("\n" + "=" * 50)
        print("You already have an appointment ^^".center(50))
        print("=" * 50)
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
    address = input("Enter your address: ").upper()
    print("=" * 50)
    mobileNum = input("Enter your mobile #: ")
    print("=" * 50)
    concern = input("Enter your concern: ").capitalize()
    print("=" * 50)

    appointment = supabase.table("appointments").insert({
        "username": username,
        "status": "pending",
        "firstname": firstName,
        "lastname": lastName,
        "middlename": middleName,
        "age": age,
        "sex": sex,
        "address": address,
        "mobilenum": mobileNum,
        "concern": concern
    }).execute()

    id = appointment.data[0]["id"]
       

    print("\n"+"=" * 50)
    print(f"Appointment booked successfully: Your ID is {id} ")
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

