# coding=utf-8
"""
折纸问题
【题目】
请把一段纸条竖着放在桌子上，然后从纸条的下边向上方对折1次，压出折痕后展开。此时
折痕是凹下去的，即折痕突起的方向指向纸条的背面。如果从纸条的下边向上方连续对折2
次，压出折痕后展开，此时有三条折痕，从上到下依次是下折痕、下折痕和上折痕。给定一
个输入参数N，代表纸条都从下边向上方连续对折N次，请从上到下打印所有折痕的方向。
例如：N=1时，打印：
down
N=2时，打印：
down
down
up
"""
result = []


def print_process(i, N, up):
    if i > N:
        return
    print_process(i + 1, N, True)
    result.append('up' if up == True else 'down')
    print_process(i + 1, N, False)


def print_all_folds(N):
    print_process(1, N, False)
    result.reverse()
    return result


if __name__ == '__main__':
    print print_all_folds(3)
