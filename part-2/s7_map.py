
# statement = ['atm add 2000', 'atm sub 500', 'atm add 2000', 'atm sub 200']
# print("Before Statement: ", statement)

add = [' 2000', ' 2000', ' 2000', ' 200']
oper = ['add', 'sub', 'add', 'opsuber']

statement = list(map(lambda x, y: 'atm ' + x + y, oper, add))

print("Before maping")
print("ADD: ", add, "\nSUB: ", oper)
print("\nAfter maping Statement: ", statement)
