class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

b = B()
b.greet()   # Output: Hello from A
