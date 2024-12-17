'''
class Emp:
    emp_count = 0
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        Emp.emp_count += 1
    def displayEmp(self):
        print('total emp count %d'%Emp.emp_count)
    def displaysal(self):
        print('name ',self.name,'sal',self.sal)

x1 = Emp('lak',1343)
x2 = Emp('lak1',11343)
x1.displayEmp()
x2.displaysal()
x1.displaysal()

##############

class Parent:
    parentAttri = 100
    def __init__(self):
        print("calling the parent constructor")
    def parentMethod(self):
        print("calling parent method")
    def setAttr(self,attr):
        Parent.parentAttri = attr
    def getAttr(self):
        print("parent attr",Parent.parentAttri)

class child(Parent):
    def __init__(self):
        print("calling from child")
    def childMethod(self):
        print("calling from child method")

c = child()
c.childMethod()
c.parentMethod()
c.setAttr(100)
c.getAttr()
###############3

########
class Vector:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def __repr__(self):
       return ("i'm in repr")

   def __str__(self):
       return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self, other):
       return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


def KelvinToFahrenheit(Temperature):
  assert (Temperature >= 0),"Colder than absolute zero!"
  return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))


########

try:
    fh = open("testfilew.txt","r")
    fh.write("this is my exception handling")
except IOError:
    print("cant find file or read")
else:
    print("written content in the file successfully")
    fh.close()
'''

try:
    fh = open("testfile1","r")
    try:
        fh.write("this is my exception hnadling")
    finally:
        print("going to close the file")
        fh.close()
except IOError:
    print("Error cant find the file")