import sys


def get_cow_number(n):
    cow_number_array = [1,2,3,4]
    # basecase
    while len(cow_number_array) < n:
        cow_number_array.append(cow_number_array[-1] + cow_number_array[-3])
    return cow_number_array[n-1]

try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print get_cow_number(int(lines[0]))
except:
    pass

