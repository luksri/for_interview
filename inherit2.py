class A(object):
    def __init__(self):
        super(A,self).__init__()
        print('A')

class B(object):
    def __init__(self):
        super(B,self).__init__()
        print('B')

class C(B,A):
    def __init__(self):
        super(C,self).__init__()
        print('C')

obj = C()

