from supabase import create_client

url = "https://kxgaxtbumeyslygazjek.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt4Z2F4dGJ1bWV5c2x5Z2F6amVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjkzNDA5MDUsImV4cCI6MjA4NDkxNjkwNX0.iUEUx5Dy2rSAbMTQr3LN6L74gyzoshhLO4ZREyI9Mto"

supabase = create_client(url, key)

# Add Contact
def addContact():
    print("\n" + "=" * 50)
    print("^^ ADD CONTACT ^^".center(50))
    print("=" * 50)
    name = input("Enter the name: ")
    print("=" * 50)
    phone = input("Enter phone #: ")
    print("=" * 50)

    print("\n" + "=" * 50)
    supabase.table("contacts").insert({
        "name": name,
        "phone": phone
    }).execute()
    print("=" * 50)

    print("\n" + "=" * 50)
    print("Add contact has been added successfully: ")
    print("=" * 50)

# View Contact
def viewContact():
    print("\n" + "=" * 50)
    print("^^ View Contacts ^^".center(50))
    print("=" * 50)
    response = supabase.table("contacts").select("*").execute()

    for contact in response.data:
        print("\n" + "-" * 50)
        print(f"{contact['id']}. Name: {contact['name']}")
        print(f"Phone #: {contact['phone']}")

# Search Contact
def searchContact():
    print("\n" + "=" * 50)
    name = input("Enter the contact name: ")
    print("=" * 50)
    response = supabase.table("contacts") \
        .select("*") \
        .eq("name", name) \
        .execute()
    
    for data in response.data:
        print("\n" + "-" * 50)
        print(f"{data['id']}. Name: {data['name']}")
        print(f"Phone #: {data['phone']}")

# Update Contact
def updateContact():
    print("\n" + "-" * 50)
    print("^^ Update Contact ^^".center(50))
    print("=" * 50)

    response = supabase.table("contacts").select("*").execute()
   

    for contact in response.data:
        print("\n" + "-" * 50)
        print(f"{contact['id']}. Name: {contact['name']}")
        print(f"Phone #: {contact['phone']}") 

    print("\n" + "=" * 50)
    contactId = int(input("Enter the id: "))
    print("=" * 50)
    updateName = input("Enter the updated name: ")
    print("=" * 50)
    updateNum = input("Enter the updated number: ")
    print("=" * 50)

    updateResponse = supabase.table("contacts") \
        .update({"name": updateName, "phone": updateNum}) \
        .eq("id", contactId) \
        .execute()
    
    print("Info updated successfully ^^")

# Delete Contact
def deleteContact():
    print("\n" + "-" * 50)
    print("^^ Delete Contact ^^".center(50))
    print("=" * 50)

    response = supabase.table("contacts").select("*").execute()
   

    for contact in response.data:
        print("\n" + "-" * 50)
        print(f"{contact['id']}. Name: {contact['name']}")
        print(f"Phone #: {contact['phone']}") 
    print("\n" + "=" * 50)
    deleteId = int(input("Enter the id you want to delete: "))
    print("=" * 50)
    deleteResponse = supabase.table("contacts") \
        .delete() \
        .eq("id", deleteId) \
        .execute()
    
    print("=" * 50)
    print("Deleted successfully ^^ ")
    print("=" * 50)

# Main Function
while True:
    print("\n" + "=" * 50)
    print("1. Add Contact".center(50))
    print("2. View All Contacts".center(56))
    print("3. Search Contacts".center(54))
    print("4. Update Contact".center(54))
    print("5. Delete Contact".center(54))
    print("6. Exit".center(44))
    print("=" * 50)

    choice = int(input("Enter your choice: "))
    print("=" * 50)
    if choice == 1:
        addContact()
    elif choice == 2:
        viewContact()
    elif choice == 3:
        searchContact()
    elif choice == 4:
        updateContact()
    elif choice == 5:
        deleteContact()
    else:
        print("Invalid choice ^^")
