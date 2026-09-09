# You are given stock prices where:

# prices[i] = price on day i

# You can buy once and sell once.

# Find the maximum profit.

# Example:

# prices = [7, 1, 5, 3, 6, 4]

# Answer:

# 5

# Because:

# buy at 1
# sell at 6

# profit = 6 - 1 = 5
# Constraints

# You cannot sell before you buy.
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            max_profit = max(max_profit, i-min_price)
    return max_profit