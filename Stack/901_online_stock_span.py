"""
LeetCode #901: Online Stock Span

Design an algorithm that collects daily price quotes and returns the span of the stock's price for the current day. The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

Constraints:
1 <= price <= 10^5, At most 10^4 calls will be made to next.
"""
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

stockSpanner = StockSpanner()
print(stockSpanner.next(100)) 
print(stockSpanner.next(80)) 
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60)) 
print(stockSpanner.next(75))
print(stockSpanner.next(85)) 
