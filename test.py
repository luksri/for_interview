'''
counter = 0
while(counter < 9):
    print(counter)
    counter = counter + 1
else:
    print("counter reached to more than 9")
print("good byeee!!!!")


for letter in 'python':
    print(letter,end='')


for letter in 'python':
    if letter == 'h':
        pass
        print("\nthis is pass block")
    print(letter,end='')

print('\n')

for letter in 'python':
    if letter == 'h':
        continue
        print("this is pass block")
    print(letter,end='')


a = [12,'dsgf','afdsg']
print(a.append(200))   ### can't print like this. these are two operations
print(a)


dict1 = {'name:': 'zara', 'age': 20}
print(len(dict1))
dict1.clear()
print(len(dict1))
'''
dict1 = {'name:': 'zara', 'age': 20}

dict2 = dict1.copy()
print(dict2)
dict2['lastname']='rao'
print(dict1)
print(dict2)
dict2['name:']='lakshman'
print(dict2)
print(dict1)