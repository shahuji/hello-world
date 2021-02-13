import sys
import os


def file_read_from_tail(fname):
    try:
        with open(fname) as f:
            r = f.read().split('\n')
            print(r[-1])
    except FileNotFoundError as e:
        print("File not Found. ", e)


file_read_from_tail('test.txt')
