class StockSpanner:

    def __init__(self):
        # plain stock price in time order
        self.stock_price = []
        # monotonic queue for stock price by day
        self.stack = []

    def next(self, price: int) -> int:
        self.stock_price.append(price)
        idx = len(self.stock_price)-1
        while self.stack and price >= self.stock_price[self.stack[-1]]:
            self.stack.pop()
        if self.stack:
            spanner = idx - self.stack[-1]
        else:
            spanner = idx+1
        self.stack.append(idx)
        return spanner