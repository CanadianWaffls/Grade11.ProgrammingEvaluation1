#lists all possible letter grades and extras
letterGradeList = ["None because you cheated!", "A+", "A", "A-", "B+", "B", "B-", 
                "C+", "C", "C-", "D+", "D", "D-", "F", "Z-" ]

#defines the letterGrade variable so that it is not considered as a local variable in a 
#later if statement so it can be used elswhere in the code
letterGrade = ""

#accepts user inputs for course grades
c1 = int(input("What percent did you get for the first course?"))
c2 = int(input("What percent did you get for the second course?"))
c3 = int(input("What percent did you get for the third course?"))
c4 = int(input("What percent did you get for the fourth course?"))

#calculates the average percent of the course grades rounded to the nearest whole number
averagePercent = int(round((c1 + c2 + c3 + c4) / 4))

#determines the user's letter grade based on thier average percent
if(averagePercent > 100): #detects if the user's grade is above the normal range
  letterGrade = letterGradeList[0]

elif(averagePercent <= 100 and averagePercent >= 95): #checks if the user's grade is 
                                                      #between a certain range
  letterGrade = letterGradeList[1] #assigns letterGrade to a value in letterGradeList
  
elif(averagePercent <= 94 and averagePercent >= 87):
  letterGrade = letterGradeList[2]
  
elif(averagePercent <= 86 and averagePercent >= 80):
  letterGrade = letterGradeList[3]
  
elif(averagePercent <= 79 and averagePercent >= 77):
  letterGrade = letterGradeList[4]
  
elif(averagePercent <= 76 and averagePercent >= 72):
  letterGrade = letterGradeList[5]
  
elif(averagePercent <= 71 and averagePercent >= 70):
  letterGrade = letterGradeList[6]
  
elif(averagePercent <= 69 and averagePercent >= 67):
  letterGrade = letterGradeList[7]
  
elif(averagePercent <= 66 and averagePercent >= 63):
  letterGrade = letterGradeList[8]
  
elif(averagePercent <= 62 and averagePercent >= 60):
  letterGrade = letterGradeList[9]
  
elif(averagePercent <= 59 and averagePercent >= 57):
  letterGrade = letterGradeList[10]
  
elif(averagePercent <= 56 and averagePercent >= 54):
  letterGrade = letterGradeList[11]
  
elif(averagePercent <= 53 and averagePercent >= 50):
  letterGrade = letterGradeList[12]
  
elif(averagePercent <= 49 and averagePercent >= 0):
  letterGrade = letterGradeList[13]
  
else: #if the user's grade does not match any other ranges it is below the normal range
  letterGrade = letterGradeList[14]

#prints the average percent and letter grade to the user
print("\nYour average percent is: ", averagePercent,"%\nYour letter grade is: ",
      letterGrade, sep='')
