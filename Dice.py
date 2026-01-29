<<<<<<< HEAD
import random
random_number_1_to_6 = random.randint(1, 6)
random_number_6_to_1 = random.randint(1, 6)
print(random_number_1_to_6)
print(random_number_6_to_1)

temp = int(random_number_1_to_6 + random_number_6_to_1)

print(temp)

if temp % 2 == 0:
    print("even")
else:
=======
import random
random_number_1_to_6 = random.randint(1, 6)
random_number_6_to_1 = random.randint(1, 6)
print(random_number_1_to_6)
print(random_number_6_to_1)

temp = int(random_number_1_to_6 + random_number_6_to_1)

print(temp)

if temp % 2 == 0:
    print("even")
else:
>>>>>>> df5b1f6 (file uploads)
    print("odd")