import re as r
"""
filter(function, sequence)
Parameters:
function: function that tests if each element of a
sequence true or not.
sequence: sequence which needs to be filtered, it can
be sets, lists, tuples, or containers of any iterators.
"""


def fun(seq):
    reg = '^[0-9]+$'
    if r.search(reg, seq):
        return True
    else:
        return False
    # letters = ['a', 'e', 'i', 'o', 'u']
    # if seq in letters:
    #     return True
    # else:
    #     return False


# sequ = ['v', 'i', 's', 'h', 'a', 'l', 's', 'h', 'a', 'h', 'u']
# sequ = set(filter(fun, sequ))

sequ = ['1', '0', 'q', '0', 'a', '8']
sequ = set(filter(fun, sequ))
print("Filter sequ are: ", list(sequ))
