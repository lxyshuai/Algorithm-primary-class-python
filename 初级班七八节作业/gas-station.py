# coding=utf-8
"""
There are N gas stations along a circular route, where the amount of gas at station i isgas[i].

You have a car with an unlimited gas tank and it costscost[i]of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
1.如果从start无法走到end，那么从start到end中的任意一个站点出发都无法走到end，所以只能退回去找可能的start。
2.如果最终sum>0，则必然存在一个解。
"""


def get_start_gas_station(cost_array, gas_station_array):
    start_index = len(gas_station_array) - 1
    end_index = 0
    sum = gas_station_array[start_index] - cost_array[start_index]
    while start_index > end_index:
        if sum > 0:
            sum += gas_station_array[end_index] - cost_array[end_index]
            end_index += 1
        else:
            start_index -= 1
            sum += gas_station_array[start_index] - cost_array[start_index]

    return start_index if sum >= 0 else -1
