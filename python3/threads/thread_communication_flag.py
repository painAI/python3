from threading import *
from time import *


class Producer:

    def __init__(self):
        self.products = []
        self.flag = False

    def produce(self):
        for i in range(1, 5):
            self.products.append("Product" + str(i))
            sleep(1)
            print("Item added")
        self.flag = True


class Consumer:

    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while not self.prod.flag:
            print("Waiting for an order")
            sleep(0.2)

        print("Order Shipped", self.prod.products)


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
