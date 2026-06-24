#recursion factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

#recursion fibonacci
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1 
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))

#checking duplicates
def contains_duplicate(nums):
    seen=set(nums)
    if len(seen)<len(nums):
        return True
    else:
        return False
    
print(contains_duplicate([1,2,3,4,5]))
print(contains_duplicate([1,2,3,4,5,1]))
