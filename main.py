import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)

pick = random.randint(0, length - 1)                                              #specifically choice() was not used.

print(f"{names[pick].title()} is going to buy the meal today!")
