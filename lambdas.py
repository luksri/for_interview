
(lambda :print('hello'))()

z = lambda a=2:print('hello',a)
z()

(lambda a=1,b=2: print(a,b))()

o = lambda x=1,y=2,z=3:print(x,y,z)
o(2,3)
o(1)


o = lambda :print(a+b)
a,b = 1,9
o()

numbers = [0,1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%3==0,numbers)))

'''


z = [1,2,3,4,5]
(lambda a,b: print(a,b),z)()
'''