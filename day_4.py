#index

text='india'
index=0
for i in text:
    print("text[", index, "]= ",i)
    index+=1

#functions
str="Hii Aparna"
print(str.swapcase())
print(str.upper())
print(str.lower())
print(str.capitalize())

str="hii aparna"
print(str.split())


print('-'.join(['india','is','great']))


#position
str="aparna"
print(str[4:6])


#string import

import string
print(type(string.digits))
print(string.ascii_letters)
print(string.digits)


str1=("hello")
print(dir(str1))



#match import

import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.match(p1,str1):
    print("found")
else:
    print(p1,"not found in str1")
p2="she"
if re.match(p2,str1):
    print("match found")
else:
    print(p1,"not present in string")



import re
str1="she sells sea shells at sea shore"
p1="sea"
rep="occean"
ns=re.sub(p1,rep,str1,1)
print(ns)


vowels =['a','e','i','o','u']
str="hello"
for i in str:
    if str==vowels:
        print("vowels present")


import re
p =r"[aeiou]"
if re.search(p,"clue"):
    print('matchy vowel')


#check anagram or not

str1="silent"
str2="listen"
s=len(str1)
l=len(str2)
if (s==l):
    sorted(str1)==sorted(str2)
    print("anagram")

else:
    print("not an anagram")


#check anagram or not

str1="race"
str2="acer"
s=len(str1)
l=len(str2)
if (s==l):
    sorted(str1)==sorted(str2)
    print("anagram")

else:
    print("not an anagram")


#zfill()
    
str='66'
print (str.zfill(4))

#geometric series(0,0,2,1,4,2,6,3..)
    
term=int(input("enter the number"))
if term%2==0:
    term=term//2
    print(term-1)
    
else:
    term=term//2+1
    term=2*(term-1)
    print(term)


#Binary data problem


size=int(input("enter the size of bin:"))  
max=count=flag=0
x=input()
arr=list(x)
for i in range(0,size):
    if arr[i]=='1':
        count= count+ 1;
        flag=1;
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)





