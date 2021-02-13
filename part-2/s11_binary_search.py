# List in binary search must be in sort form
pos = -1


def search(cont, j):
    l = 0
    u = len(cont) - 1

    while l <= u:
        mid = (l + u) // 2

        if cont[mid] == j:
            globals()['pos'] = mid
            return True
        else:
            if cont[mid] < j:
                l = mid
            else:
                u = mid


content = [12, 34, 56, 78, 90, 23, 45, 67, 89]
content.sort()  # [12, 23, 34, 45, 56, 67, 78, 89, 90]
print(content)
n = 56

if search(content, n):
    print(f"Get {n} at position: {pos}")
else:
    print("Not in content", n)
