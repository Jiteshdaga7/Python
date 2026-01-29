print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? \n"))
tip = int(input("How Much tip you would like to give? \n 10, 12 or 15 \n"))
people = int(input("How many people to split the bill? \n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")