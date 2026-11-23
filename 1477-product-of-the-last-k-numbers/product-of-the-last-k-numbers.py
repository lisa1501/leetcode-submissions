class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        

    def add(self, num: int) -> None:
        self.arr.append(num)
        

    def getProduct(self, k: int) -> int:
        product = 1
        l = len(self.arr)
        for num in self.arr[(l-k):]:
            product *=  num
        return product
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)