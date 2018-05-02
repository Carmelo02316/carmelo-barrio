math_grade = input("enter your current math grade:")
science_grade = input("enter your current science grade:")
english_grade = input("enter your current english grade:") 
gym_grade = input("enter your gym current grade:")
history_grade = input("enter your current history grade:")

grade_list = [math_grade, science_grade, english_grade, gym_grade, history_grade]

average = (int(math_grade) + int(science_grade) + int(english_grade) + int(gym_grade) + int(history_grade)) / 5

grade_list.append(average)

print " The last number on the list is your average."       

print str(grade_list)

if average < 60:
    print" you are failing!"
elif average >= 60 and average < 70:
    print " panic, you have a D!"
elif average >= 70 and average < 80:
    print " you have a C so keep working so you can get up to a B."
elif average >= 80 and average < 90:
    print " you are doing good, you have a B."
elif average >= 90 and average <= 100:
    print " awesome, you have an A!"
    
