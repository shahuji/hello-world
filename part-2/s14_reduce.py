from functools import reduce

# Getting total amount after all transaction

statement = ['atm add 2000', 'atm sub 500', 'atm add 2000', 'atm sub 2000']
number = []

for i in statement:
    for word in i.split():
        if word.isnumeric():
            if i.__contains__("add"):
                number.append(int(word))  # If amount store in + is deposit
            else:
                number.append(-int(word))  # If amount store in - is sub(withdraw)

balaance = reduce(lambda a, b: a + b, number)
print("All transact values are: ", number)
print("Available balance is: ", balaance)
