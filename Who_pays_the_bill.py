# Who pays the bill?

import random
friends = ["Jitesh", "Ankit", "Deepak", "Suresh", "Ramesh"]
bill_amount = float(input("Enter the total bill amount: $"))
payer = random.choice(friends)
print(f"{payer} is going to pay the bill of ${bill_amount:}")
