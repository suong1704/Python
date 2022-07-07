# s = {'1',1,2,(1,2,3)}

# #hash object unhas object
# c = 'asd'
# print(id(c))
# c = 'dfd'
# print(id(c))

# li = [1,12,3]
# print(id(li))
# li += '5'
# print(id(li))

# d = {'MSSV':1, 'Name':'NVA'}
# d1 = dict({'MSSV':1 , 'Name':'NVA'})
# print(d1)
# print(d1['MSSV'])
# d2 = d1.items()
# print(d2)
# print(d1.keys())
# print(d1.values())
# d3 = dict(MSSV = 1, Name = 'NVA')

# s = 'asdsf'
# i = 0
# while i< len(s):
#     print(s[i])
#     i+=1
# else:
#     print('END')

# for x in range(0,3):
#     print(x)
# li = [1,2,'A']
# for x in li:
#     print(x)
# d = {'MSSV':1 , 'Name':'NVA'}
# for k , v in d.items():
#     print(k,':',v)

def A(a:int, b:str):
    print('a =', a, ',b =',b)
    return a,b
a,c =A(1,'safsdd')
print(a,c)

 