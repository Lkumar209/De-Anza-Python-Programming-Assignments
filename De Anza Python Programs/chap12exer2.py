class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            result = self.current
            self.current, self.next = self.next, self.current + self.next
            self.count += 1
            return result
        else:
            raise StopIteration

def fibonacci_generator(n):
    current = 0
    next = 1
    count = 0
    while count < n:
        yield current
        current, next = next, current + next
        count += 1

iterator = FibonacciIterator(10)
print("Fibonacci numbers using iterator:")
for num in iterator:
    print(num, end=' ')
print()

generator = fibonacci_generator(10)
print("Fibonacci numbers using generator:")
for num in generator:
    print(num, end=' ')
print()


'''
Fibonacci numbers using iterator:
0 1 1 2 3 5 8 13 21 34 
Fibonacci numbers using generator:
0 1 1 2 3 5 8 13 21 34 

'''