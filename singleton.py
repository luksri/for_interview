# class singleton(type):
#     def __new__(cls, *args,**kwargs):
#         super().__new__()
#         cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__call__(*args,**kwargs)
#         return cls._instance
#
# class Meta(metaclass=singleton):
#     pass
#
# def m():
#     m1 = Meta()
#
# m()
class Singleton:
    _instance = None
    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        print("im here")
        if Singleton._instance != None:
            raise Exception("Cant create one more instance")
        Singleton._instance = self
s=Singleton()
print(s.getInstance(), id(s.getInstance()))
print(s.getInstance(), id(s.getInstance()))
print(s.getInstance(), id(s.getInstance()))