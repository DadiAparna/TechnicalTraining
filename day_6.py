#program to create and access an obj

class abc:
    var=10
obj = abc()
print(obj.var) 

#to create self arg and access an obj


class abc:
    attribute1=10
    def display(self):
        print("this is in class")  
obj=abc()
print(obj.attribute1)
obj.display()


# to check the use of a constructor

class abc:
    def _int_(self,value):
        print("this is in the class")
        self.value=value
        print("the value is",value)
    
obj = abc(100)


#class variables and object variables

class abc:
    class_var = 0
    def _int_(self,var):
        abc.class_var +=1
        self.var =var
        print("the object value is",var)
        print("the class value is", abc.class_var)

obj1 = abc(100)
obj2 = abc(101)
obj3 = abc(102)


#even odd finding

class number:
    even=0
    def check(self,num):
        if num%2 ==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num, "iseven")
        else:
            print(num, "is odd")

n=number()
n.even_odd(21)

# sorting even and odd in a list

class Number:
    even=[]
    odd=[]
    def _int_ (self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1 = Number(11)
n2 = Number(12)
n3 = Number(13)
n4 = Number(17)
n5 = Number(28)

print("even number list is",Number.even)
print("odd number list is",Number.odd)



# write a program that has a class circle.use a class variable to define the values of const pi.use class variable to calculate the area & circumference of the circle with specified radius. where radius=4.5
class circle:
    pi = 3.14159
    def _int_(self, r):
        self.r = r
    def area(self):
        return (circle.pi*self.r*self.r)
    def circum(self):
        return (2*circle.pi*self.r)
c = circle(4.5)
print("area=",c.area())
print("circumference",c.circum())                


