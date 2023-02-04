
def _sum(a, b):
    return a+b 

def sub(a, b):
    return a-b 

def mul(a, b):
    return a*b 

def div(a, b):
    return a/b 

def modulo(a, b):
    if a > b:
        return a - b 
    else:
        return b - a 

a, b = 5, 6 

print(_sum(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))
print(modulo(a, b))




