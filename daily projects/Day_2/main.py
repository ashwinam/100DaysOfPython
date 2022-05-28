#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Bannner
print("Welcome to the Tip Calculator")
bill_amt = float(input("What was the total bill amount? ₹"))
tip_percentage = int(input("What percentage tip would you like to give? e.x. 10, 12 & 15? "))
total_bill_amt = bill_amt * (1+(tip_percentage/100))
per_person_amt = int(input("How many People to split the bill? "))
print(f"Each person should pay {total_bill_amt/per_person_amt:.2f}")