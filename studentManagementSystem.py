student = {}
studentsAcc = {}
teachersAcc = {}



def studentDashboard():
    print("=" * 50)
    print("1. Check Info".center(50))
    print("2. Grade".center(50))
    print("=" * 50)

    
def teacherDashboard():
    pass


def studentAcc():
    studentUser = input("Enter your username: ")
    studentPass = input("Enter your password: ")

    studentsAcc[studentUser] = studentPass
    print(f"Account {studentUser} has been created successfully")
    return

def teacherAcc():
    teacherUser = input("Enter your username: ")
    teacherPass = input("Enter your password: ")

    teachersAcc[teacherUser] = teacherPass
    print(f"Account {teacherUser} has been created successfully")
    return

def addStudent():
    pass
def updateStudent():
    pass
def deleteStudent():
    pass
def viewStudents():
    pass
def signUp():
    while True:
        print("=" * 50)
        print("1. Student Account".center(50))
        print("2. Teacher Account".center(50))
        print("3. Exit".center(40))
        print("=" * 50)

        choice = int(input("Enter your choice: "))
        if choice == 1:
            studentAcc()
            return
        elif choice == 2:
            teacherAcc()
            return
        elif choice == 3:
            break
        else:
            print("Invalid input")
def signIn():
    User = input("Enter your username: ")
    Pass = input("Enter your password: ")

    if not studentsAcc and teachersAcc:
        print("User not found")
    elif studentsAcc[User] == Pass:
        studentDashboard()
        return
    elif teachersAcc[User] == Pass:
        teacherDashboard()
        return
    else:
        print("Incorrect Password")

    
while True:
    print("=" * 50)
    print("1. Sign Up".center(50))
    print("2. Sign In".center(50))
    print("3. Exit".center(48))
    print("=" * 50)
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        signUp()
    elif choice == 2:
        pass
    elif choice == 3:
        break
