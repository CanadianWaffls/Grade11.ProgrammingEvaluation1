#-----Question 1-----

#Title for this question
print("My Name in Ascii Art")

#prints my name in ascii art
print("""         o           o                         
        <|>         <|>                        
        / \         / \                        
      o/   \o       \o/    o__  __o   \o    o/ 
     <|__ __|>       |    /v      |>   v\  /v  
     /       \      / \  />      //     <\/>   
   o/         \o    \o/  \o    o/       o/\o   
  /v           v\    |    v\  /v __o   /v  v\  
 />             <\  / \    <\/> __/>  />    <\ \n""")
#-----Question 2-----

#imports the math library
import math

#Title for this question
print("Area of a Triangle")

#asks the user to input side lengths of a triangle
a = int(input("What is the first side length of the triangle? "))
b = int(input("What is the second side length of the triangle? "))
c = int(input("What is the third side length of the triangle? "))

#defines the variable s used for the final area
s = (a + b + c) / 2

#calculates the final area of the triangle using the user inputs, the s variable and the 
#sqrt function imported from math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

#prints the the area of the triangle rounded to 2 decimals
print("\nThe area of the triangle is", round(area, 2), "Units squared\n")
#-----Question 3-----

#imports the random library
import random

#asks for the user's budget
totalBudget = int(input("What is your budget? "))

#generates random percentage values for food, clothing, entertainment, and rent
foodPercent = random.randint(17, 23)
clothingPercent = random.randint(3, 9)
entertainmentPercent = random.randint(1, 7)
rentPercent = random.randint(67, 73)

#checks to make sure the item percantages equal 100
finalPercent = foodPercent + clothingPercent + entertainmentPercent + rentPercent

#if the percent is not equal to 100 it will perform this code until it is equal to 100
while(finalPercent != 100):
  #checks if the percentage is lower than 100
  if(finalPercent < 100):
    #gets the lowest value of the percents
    minimum = min(foodPercent, clothingPercent, entertainmentPercent, rentPercent)
    #adds 1 to the lowest percent 
    if foodPercent == minimum:
      foodPercent += 1
    elif clothingPercent == minimum:
      clothingPercent += 1
    elif entertainmentPercent == minimum:
      entertainmentPercent += 1
    else:
      rentPercent += 1
  #checks if the percentage is higher than 100
  if(finalPercent > 100):
    #gets the highest value of the percents
    maximum = max(foodPercent, clothingPercent, entertainmentPercent, rentPercent)
    #subtracts 1 from the highest percent
    if foodPercent == maximum:
      foodPercent -= 1
    elif clothingPercent == maximum:
      clothingPercent -= 1
    elif entertainmentPercent == maximum:
      entertainmentPercent -= 1
    else:
      rentPercent -= 1
  #re-calculates the added percentages so the program can continue or keep adjusting 
  #until it equals 100
  finalPercent = foodPercent + clothingPercent + entertainmentPercent + rentPercent

#finds the money amount of thebudget items from the percentages
food = round((totalBudget / 100) * foodPercent)
clothing = round((totalBudget / 100) * clothingPercent)
entertainment = round((totalBudget / 100) * entertainmentPercent)
rent = round((totalBudget / 100) * rentPercent)

#prints out the total budget, the cost of each item, and the percentage of each item to 
#the user
print("Total budget: $", totalBudget, sep='')
print("Budget item costs: ", "Food $",food, ", Clothing $",clothing,
  ", Entertainment $",entertainment, ", Rent $", rent, sep='')
print("Budget item percentages: ", "Food ", foodPercent,"%, ",
      "Clothing ", clothingPercent,"%, ",
      "Entertainment ", entertainmentPercent,"%, ",
      "Rent ", rentPercent,"%", sep='')
