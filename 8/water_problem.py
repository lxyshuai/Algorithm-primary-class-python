# coding=utf-8
"""
给定一个数组代表一个容器，
比如[3,1,2,4]，
代表0位置是一个宽度为1，高度为3的直方图。
代表1位置是一个宽度为1，高度为1的直方图。
代表2位置是一个宽度为1，高度为2的直方图。
代表3位置是一个宽度为1，高度为4的直方图。
所有直方图的底部都在一条水平线上，且紧靠着。
把这个图想象成一个容器，这个容器可以装3格的水。
给定一个没有负数的数组arr，返回能装几格水？
"""


class Solution(object):
    def trap1(self, height):
        """
        一个位置上能装水的值由其左边和右边的最大值中较的一个决定
        第一种解法通过预处理数组记录所有位置左边右边的最大值
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)
        # left_max_array左边最大数组,N位置代表0~N位置上的最大值
        left_max_array = []
        left_max_array.append(height[0])
        # 从左边向右遍历一次,得到left_max_array
        for index in range(1, length, 1):
            if height[index] > left_max_array[index - 1]:
                left_max_array.append(height[index])
            else:
                left_max_array.append(left_max_array[index - 1])
        # right_max_array左边最大数组,N位置代表N~length位置上的最大值
        right_max_array = [0 for _ in range(length)]
        right_max_array[-1] = (height[-1])
        # 从右向左遍历一次,得到right_max_array
        for index in range(length - 2, -1, -1):
            if height[index] > right_max_array[index + 1]:
                right_max_array[index] = height[index]
            else:
                right_max_array[index] = right_max_array[index + 1]

        sum = 0
        # 再遍历一次数组,得到每个位置的水量
        for index in range(1, length - 1, 1):
            min_of_max = min(left_max_array[index], right_max_array[index])
            if height[index] >= min_of_max:
                sum += 0
            elif height[index] < min_of_max:
                sum += (min_of_max - height[index])
        return sum

    def trap2(self, height):
        """
        不需要额外数组,用两个变量记录左右部分最大值
        :return:
        :rtype:
        """
        if not height:
            return 0
        length = len(height)
        if length < 3:
            return 0
        # 记录0~current_left_index-1上的最大值
        left_max = height[0]
        # 记录current_right_index+1~length上的最大值
        right_max = height[length - 1]
        current_left_index = 1
        current_right_index = length - 2
        sum = 0
        while current_left_index <= current_right_index:
            # left_max < right_max时能确定current_left_index左边的最大值
            if left_max < right_max:
                if height[current_left_index] >= left_max:
                    sum += 0
                    left_max = height[current_left_index]
                else:
                    sum += left_max - height[current_left_index]
                current_left_index += 1
            # right_max < left_max时能确定current_right_index右边的最大值
            else:
                if height[current_right_index] >= right_max:
                    sum += 0
                    right_max = height[current_right_index]
                else:
                    sum += right_max - height[current_right_index]
                current_right_index -= 1
        return sum
if __name__ == '__main__':
    print Solution().trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
