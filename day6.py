#anagram problem
def func():
    word1=input('enter first word: ')
    word2=input('enter second word: ')
    if sorted(word1)==sorted(word2):
        print('yes,anagram-method 1')
    else:
        print('not anagram-method 1')
    d1={}
    d2={}
    for char in word1:
        if char in d1:
            d1[char]+=1
        else:
            d1[char]=1
    for char in word2:
        if char in d2:
            d2[char]+=1
        else:
            d2[char]=1
    if d1==d2:
        print('yes,anagram-method 2')
    else:
        print('not anagram-method 2')
func()


#palindrome problem
def is_palindrome(s):
    s=s.lower()
    for i in range(len(s)//2):
        if s[i]==s[len(s)-i-1]:
            continue
        else:
            print('not palindrome')
            break
    else:
        print('palindrome')
is_palindrome('racecar')
is_palindrome('hello')

#sliding window problem
stock=eval(input('enter list of stock prices for each day in the form of list'))
min_price=stock[0]
max_profit=0
for price in stock:
    if min_price>price:
        min_price=price
    if price-min_price>max_profit:
        max_profit= price-min_price
print('max profit is:',max_profit)
