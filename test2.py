'''
sum = (lambda x,y: x+y)
print(sum(3,4))

### same as normal function calculates the sum and return the value.####

a = input('value for x: ')
b = input('value for y: ')
print(sum(int(a),int(b)))


def fht(T):
    return ((float(9)/5)*T+32)

def cel(T):
    return  (float(5)/9)*(T-32)

temp = (36.5,37,37.5,40)

F = map(fht,temp)
C = map(cel,F)

print(list(F),list(C))

F = list(map(fht,temp))
C = list(map(cel,F))

print(F,C)


alph = ['a','b','c','i','j','o']

def filvow(alphe):
    vowels = ['a','e','i','o','u']

    if(alphe in vowels):
        return True
    else:
        return False
result = filter(filvow,alph)
print(result)
for v in result:
    print(v)


def outertext(text):
    text = text

    def innertext():
        print(text)
    return (innertext)


if __name__ == '__main__':
    myfunc = outertext('hey')
    myfunc()


def shout(text):
    return (text.upper())

print(shout('hello'))

yell = shout

print(yell('hey'))
'''

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func('wjlfjlekwjlkfjeEEEEEEE')
    print(greeting)

greet(shout)
greet(whisper)