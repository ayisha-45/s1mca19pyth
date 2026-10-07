clist1=set()
clist2=set()
n1=int(input("enter number of colors in list 1:"))
print("enter the colors to list 1:")
for x in range(n1):
    color=input()
    clist1.add(color)
    n2=int(input("enter the number of colors in list2:"))
    print("enter the color to list2:")
    for x in range(n2):
        color=input()
        clist2.add(color)
        diff=clist1.difference(clist2)
        print("colors in list1 not in list2:",diff)
