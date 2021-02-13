import time
from functools import lru_cache


@lru_cache(maxsize=2)
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print('Delay start')
    some_work(1)
    print('First delay complete')
    some_work(2)
    print('Second delay complete')
    some_work(3)
    print('Third delay complete')
    some_work(1)
    print('Delay complete')
