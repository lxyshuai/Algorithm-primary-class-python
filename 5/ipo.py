# coding=utf-8
"""
输入：
参数1，正数数组costs
参数2，正数数组profits
参数3，正数k
参数4，正数m
costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
k表示你不能并行、只能串行的最多做k个项目
m表示你初始的资金
说明：你每做完一个项目，马上获得的收益，可以支持你去做下一个
项目。
输出：
你最后获得的最大钱数。
"""
import Queue


class CostProject(object):
    def __init__(self, cost=None, profit=None):
        self.cost = cost
        self.profit = profit

    def __cmp__(self, other):
        if self.cost < other.cost:
            return -1
        elif self.cost > other.cost:
            return 1
        else:
            return 0


class ProfitProject(object):
    def __init__(self, cost=None, profit=None):
        self.cost = cost
        self.profit = profit

    def __cmp__(self, other):
        if self.profit < other.profit:
            return 1
        elif self.profit > other.profit:
            return -1
        else:
            return 0


def find_maximized_capital(money, time, costs, profits):
    project_cost_pq = Queue.PriorityQueue()
    project_profit_pq = Queue.PriorityQueue()
    for _cost, _profit in zip(costs, profits):
        project_cost_pq.put(CostProject(_cost, _profit))
    for _ in range(time):
        while project_cost_pq.qsize() != 0 and project_cost_pq.queue[0].cost <= money:
            _cost_project = project_cost_pq.get()
            project_profit_pq.put(ProfitProject(_cost_project.cost, _cost_project.profit))
        if project_profit_pq.qsize() == 0:
            return money
        money += project_profit_pq.get().profit
    return money


if __name__ == '__main__':
    costs = map(int, raw_input().split())
    profits = map(int, raw_input().split())
    time = input()
    money = input()
    print find_maximized_capital(money, time, costs, profits)
