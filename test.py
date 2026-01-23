quiz = float(input("Enter your quiz score (0-100):  "))
labExercise = float(input("Enter your lab score (0-100):  "))
midExam = float(input("Enter your midterm exam score (0-100):  "))
finalExam = float(input("Enter your final exam score (0-100):  "))

finalGrade = (quiz * 0.20) + (labExercise * 0.30) + (midExam * 0.20) + (finalExam * 0.30)

print(f"Your final grade is: {round(finalGrade, 2)}")

if finalGrade >= 90 and min(quiz, labExercise, midExam, finalExam) >= 80:
    print("Eligible for honor")
else:
    print("not eligible")

