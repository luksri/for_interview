import re

line = 'Cats are smarter than cows and dogs'

#matchobj = re.match(r'(.*)are(.*?) .*',line,re.M|re.I)
matchobj = re.match(r'(.*) are (.*?) .*',line,re.I)
print(matchobj)
if matchobj:
    print("matchobj.group",matchobj.group())
    print("matchobj.group1", matchobj.group(1))
    print("matchobj.group2", matchobj.group(2))
else:
    print("no match")

######

matchobj = re.match(r'are',line,re.I)

if matchobj:
    print("matchobj.group",matchobj.group())
else:
    print("no match")

searchobj = re.search(r'dogs',line,re.M|re.I)
if searchobj:
    print(searchobj.group())
else:
    print("nothing")

#########

phone = "2004-959-559# this # is the phone number"

num = re.sub(r'#.*$','',phone)
print(num)


num = re.sub(r'\d','x',phone)
print(num)

#####

ex = " Jesseica is 15 years old." \
     "Oscar is 102." \
     "Ldward is 92." \
     "laks 123233423."
ages = re.findall(r'\d{1,3}',ex)
names = re.findall(r'[A-Z][a-z]*',ex)
print(ages)
print(names)

######

