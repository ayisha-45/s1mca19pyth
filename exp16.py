import operator
mydict={}
while True:
    key=input("enter a key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
print('original dictionary:',mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print('Dictionary in asccending order by value:',sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print('dictionary in descenting order by value:',sd)
