from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        buy_day = -1
        sell_day = -1
        min_day = -1

        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
                min_day = i
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    buy_day = min_day
                    sell_day = i

        print(f"Buy on day {buy_day} at {prices[buy_day]}, sell on day {sell_day} at {prices[sell_day]}")
        return max_profit
