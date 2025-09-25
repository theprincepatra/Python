# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 => Ex
# 80 - 90 => A
# 70 - 80 => B
# 60 - 70 => C
# 50 - 60 => D
#  <50    => F


marks = int(input("enter ur marks:"))

if(marks<=100 and marks>=90):
    print("Ex",marks)
elif(marks<=90 and marks>=80):
    print("A",marks)
elif(marks<=80 and marks>=70):
    print("B",marks)
elif(marks<=70 and marks>=60):
    print("C",marks)
elif(marks<=60 and marks>=50):
    print("D",marks)
else:
    print("F",marks)

print("END OF PROGRAM")

# Output:
# enter ur marks: 85
# A 85
# END OF PROGRAM
