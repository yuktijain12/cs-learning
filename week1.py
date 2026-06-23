#list
fruits=['apple','banana','cherry','kiwi','mango']
fruits.append('orange')
print(fruits)
fruits.insert(1,'grapes')
print(fruits)   
fruits.pop()
print(fruits)
fruits.remove('banana')
print(fruits)

#dictionary
student={'name':'John','age':10,"marks":90,'city':'New York'}
print (student['name'])
student['gender'] = 'Male'
print(student)
student['age'] = 11
print(student)
student.pop('city')
print(student)

#sets
cricket={'rahul','virat','dhoni','rohit'}
football={'rahul','rohit','messi','ronaldo'}
print('players who play both:',cricket&football)
print('players who play either:',cricket|football )
print('players who play cricket but not football:',cricket-football)

#tuple
cities=('New York','London','Paris','Tokyo','Sydney')
print(cities[0])
#cities[0]='Berlin'  # This will raise an error because tuples are immutable
print(cities.count('London'))
print(cities.index('Paris'))

