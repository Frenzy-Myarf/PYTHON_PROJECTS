from supabase import create_client

url = "https://kxgaxtbumeyslygazjek.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt4Z2F4dGJ1bWV5c2x5Z2F6amVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjkzNDA5MDUsImV4cCI6MjA4NDkxNjkwNX0.iUEUx5Dy2rSAbMTQr3LN6L74gyzoshhLO4ZREyI9Mto"

supabase = create_client(url, key)

# insert data to supabase

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# course = input("Enter your course: ")
# supabase.table("students").insert({
#     "name": name,
#     "age": age,
#     "course": course
# }).execute()

# select data from supabase
#response = supabase.table("students").select("*").execute()

# printing data
# print(response.data)

# for loop data
#for student in response.data:
#    print(student["name"], student["age"], student["course"])

print("saved")