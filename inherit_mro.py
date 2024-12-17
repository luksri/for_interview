class A(object):
    def __init__(self):
        print('inside class A')
class B(A):
    def __init__(self):
        print('inisde class B')
'''
class C(A):
    def __init__(self):
        print('inside class C')
class D(C,B):
    pass

obj = D()
'''

class C(B,A):
    def __init__(self):
        super(A).__init__()
        super(B).__init__()

print(C.mro())
obj = C()