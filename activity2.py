quiz = float(input("Enter your quiz (1-100): "))
lExercise = float(input("Enter your lab exercise (1-100): "))
midExam = float(input("Enter your midterm exam (1-100): "))
finalExam = float(input("Enter your final exam (1-100): "))

finalGrade = (quiz * 0.20) + (lExercise * 0.30) + (midExam * 0.20) + (finalExam * 0.30)

print(f"Final Grade: {finalGrade:.2f}")

if finalGrade >= 90 and min(quiz, lExercise, midExam, finalExam) >= 80:
    print("Eligible for honor")
else:
    print('not eligible')

print("(quiz + lab) / 2 > midExam: ", (quiz + lExercise) / 2 > midExam )
print("finalExam >= midterm: ", finalExam >= midExam)
print("quiz != lExercise: ", quiz != lExercise )
print("not (finalGrade < 75): ", not(finalGrade < 75))
