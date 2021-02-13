import random

str1 = " Hello this is DATA type and operator file"
print("\u2192 \N{rightwards arrow}", str1)
print(" Slicing str1=>", str1[::-1])
print(" Using random to to get string str1=>", str1[random.randrange(0, len(str1) - 5):len(str1)])
com = 2 + 3j
print(" Complex a=", com)
flt1 = .4e7
flt2 = 4.2
int1 = 4
print(" Float flt1=", flt1, "And flt2=", flt2)
print(" Int int1=", int1)

flt2 = 4.2e-4
print(" Subtraction of flt2-int1=", flt2)

bool1 = True
bool2 = False
bool3 = False
print(" True bool1=", bool1, ", False bool2=", bool2)

txt = " The best things in life are free! by Vishal"
if "free" in txt:
    print(" Yes, 'free' is present.")

elif "vishal" not in txt:
    print("Yes, 'vishal' is not present.")

a = " => Aello, World!"
print(a.replace("A", "H"))
