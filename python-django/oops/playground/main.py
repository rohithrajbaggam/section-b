
class MathClass:

    def sum(self, a, b):
        return a + b 

    def sub(self, a, b):
        return a - b 
    
    def mul(self, a, b):
        return a * b 
    
    def div(self, a, b):
        return a / b 
    
    def mod(self, a, b):
        return a % b 

class Expression(MathClass):

    def lhs(self, a, b):

        return self.mul( 
            self.sum(a, b),
            self.sum(a, b)
        )

    def rhs(self, a, b):
        sq_a = self.mul(a, a)
        sq_b = self.mul(b, b)
        ab = self.mul(a, b)
        # a^2+b^2 
        sq = self.sum(sq_a, sq_b)
        _2ab = self.sum(ab, ab)
        return self.sum(sq, _2ab)

        # return self.sum(
        #     self.sum
        #     (
        #     self.mul(a,a),
        #     self.mul(b,b)
        #     ),
        #     self.sum(
        #     self.mul(a,b),
        #     self.mul(a,b)
        #     )
        # )


obj = Expression()

print(obj.lhs(2, 3))
print(obj.rhs(2,3))

# obj = MathClass()
# print(obj.mod(2, 3))


# class FirstClass:
#     a = 1 
#     b = 2 
#     name = "max"

#     def __init__(self, name):
#         self.name = name  

#     def __str__(self):
#         return "This is my First Class"

#     def sayHello(self):
#         print(f'Hello, {self.name}')

# obj = FirstClass("Lucy")
# print(obj) 
# # print(int)
# obj.sayHello()
# print(obj.name)
    
    



