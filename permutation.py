def permutation(list1,list2):
    if len(list1) != len(list2):
        return 'Size of both lists are not same'
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    else:
        return False
list1=[1,3,2]
list2=[3,2,1]
print(permutation(list1,list2))