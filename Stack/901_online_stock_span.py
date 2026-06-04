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
