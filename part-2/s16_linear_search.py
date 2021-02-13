pos = -1


def search(content, n):
    i = 0
    while i < len(content):
        if content[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


content = [12, 23, 34, 45, 56, 67, 78, 89, 90]
n = 34

if search(content, n):
    print("Got it position in list: ", pos)
else:
    print("Not correct value.")
