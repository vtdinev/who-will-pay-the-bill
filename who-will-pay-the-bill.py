import random

all_names = input("Please enter all the names: ")
split_all_names = all_names.split(", ")
names_count = len(split_all_names)
random_number = random.randint(0, names_count- 1)
payer = split_all_names[random_number]
print(f"The bill will be paid by {payer}")
