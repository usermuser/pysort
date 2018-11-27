alist = [3, 2, 1]

def bsort(a):
    tmp = ''
    for i in range(len(a)):
        if a[i] > a[i+1]:
            a[i] = tmp
            a[i+1] = a[i]
            a[i] = tmp
    return a

# print(bsort(alist))

# for i in alist:
#     print(i)
#

print('break')
def bsort2(a):
    tmp = ''
    print(a)
    for i in range(len(a)-1):
        for i in range(len(a)):
            try:
                if a[i] > a[i+1]:
                    tmp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = tmp
                    # print(alist[i+1])
            except IndexError:
                continue
    return a

print(bsort2(alist))
# if alist[3]:
#      print('yes')
# else:
#     print('no')



