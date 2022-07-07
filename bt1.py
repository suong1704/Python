li = []
for i in range(0,5):
    a=input()
    if(a != 'done'):
        li.append(a)
def getInt(li):
    n= []
    i = 0
    while i < len(li):
        if (li[i]>='0' and li[i] <='9'):
            n.append(li[i])
        i += 1  
    return n
def swap(a,b):
    return b,a
def sortt(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if (int(li[i]) < int(li[j])):
                li[i],li[j]=swap(li[i],li[j])
    return li
li = getInt(li)
li = sortt(li)
print(li)





