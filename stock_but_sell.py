"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

def buy_sell_stock(prices):
    min_so_far = prices[0]
    max_profit = 0
    n = len(prices)
    for i in range(1, n) :
        print(prices[i] ,prices[i-1],"?????")
        if(prices[i] > prices[i-1]) :
            max_profit += (prices[i] - prices[i-1])
        
    return max_profit


prices = [7,1,5,3,6,4]
sell_num = buy_sell_stock(prices)
print(sell_num,"||||||||||||||||||||||||||||||||||||||||||||||||||")