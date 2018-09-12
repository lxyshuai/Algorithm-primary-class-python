def hanoi(n):
    process(n, 'left', 'right', 'middle')


def process(n, from_pole, to_pole, help_pole):
    if n == 1:
        print 'move ' + str(n) + ' from ' + from_pole + ' to ' + to_pole
    else:
        process(n - 1, from_pole, help_pole, to_pole)
        print 'move ' + str(n) + ' from ' + from_pole + ' to ' + to_pole
        process(n - 1, help_pole, to_pole, from_pole)


if __name__ == '__main__':
    hanoi(3)
