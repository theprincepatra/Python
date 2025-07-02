Write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user.

# Ans --- 
# signing in
marks1 = int(input("enter mark 1:"))
marks2 = int(input("enter mark 2:"))
marks3 = int(input("enter mark 3:"))

# CHECK FOR TOTAL PERCENTAGE ---
total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("YOU ARE PASS BOI",total_percentage)

else:
    print("YOU ARE FAIL,BETTER LUCK NEXT TIME GIRL",total_percentage)

print("END OF PROGRAM")
#output:
#enter mark 1: 45  
#enter mark 2: 38  
#enter mark 3: 42  
#YOU ARE PASS BOI 41.66666666666667
