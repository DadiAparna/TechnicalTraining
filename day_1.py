
#print the name in telugu
print(chr(3077)+chr(3114)+chr(3120)+chr(3149)+chr(3107))

#import
import keyword
print(keyword.kwlist)

#comparision&logical operator
a=1000
b=1500
c=-500
d=4000
print(a>b and a>c)
print(a<b and a<c and a>d)
e=2000
print(c if c<e else e)

#end()
a=30
b=20
c=50

print(a,b,c,end=" ")

#== comparing value and datatype
a=6
b=True
if(1==b):
    print("yes")
else:
    print("no")

#reverse order of alphabets
    
for i in range(122,96,-1):
    print(chr(i),end=" ")

#double for loop

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
        print("/n",)
    
#for loop

age=[2,4,6,8]
for i in range(len(age)):
    print(i)





