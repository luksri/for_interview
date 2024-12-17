class decorator_with_arguments(object):
    def __init__(self,arg1,arg2,arg3):
        print("init called")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self,f):
        print("inside call ")
        def wrapped_f(*args):
            print("inside wrapped function")
            print("decorator arguments: ",self.arg1,self.arg2,self.arg3)
            f(*args)
            print("after wrapped function executed")
        return wrapped_f

@decorator_with_arguments("hello","lakshman","rao")
def func1(a1,a2,a3,a4):
    print("the function arguments are: ",a1,a2,a3,a4)

print('after decoration')
func1("this","is","test",6)