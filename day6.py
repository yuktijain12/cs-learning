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
