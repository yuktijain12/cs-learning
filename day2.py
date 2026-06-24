#functions
def greet(name,language='English'):
    if language == 'English':
        print('Hello',name)
    elif language== 'Hindi':
        print('Namaste',name)
    elif language=='French':
        print('Bonjour',name)
greet('Yukti')
greet('Yukti','Hindi')
greet('Yukti','French')

#using args
def add_all(*args):
     print('Sum:',sum(args))
add_all(1,2,3)
add_all(4,5,6,7,8)

#using list comprehension
list=[i**2 for i in range (1,11)]
newlist=[i for i in list if i%2==0]
print(list)
print(newlist)

#scopes
count=0 
def func():
    print(count)
def func2():
    count=10
    print(count)
def func3():
    global count
    count=10
    print(count)
func()
func2()
func3()

#lambda function
func = lambda x,y: max(x,y)
print(func(2,4))
