
class entry_exit(object):
    def __init__(self,f):
        print("init called")
        self.f = f
    def __call__(self):
        print("entering ",self.f.__name__)
        self.f()
        print("exiting ",self.f.__name__)

@entry_exit
def fun1():
    print("inside func1")

@entry_exit
def func2():
    print("inside func2")

def fun3():
    print("inside fun3")

fun1()
#func2()

# f = entry_exit(fun3)
#f()
