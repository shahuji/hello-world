class top_10:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
        else:
            raise StopIteration

        return val


valu = top_10()

print("Start: ", next(valu))

for i in valu:
    print(i)
