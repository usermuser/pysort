# alist = [3, 2, 1]
# alist = [6,1,7,8,9,3,5,4,2]
alist = [6, 3, 5, 4, 2]

def bsort(a):
    for i in range(len(a)):
        if a[i] > a[i+1]:
           a[i], a[i+1] = a[i+1], a[i]
    return a


def bsort2(a):
    print('[+] Started BubbleSort for: {}'.format(alist))
    for i in range(len(a)-1):
        for j in range(len(a)):
            try:
                if a[j] > a[j+1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
            except IndexError:
                continue
    return print('[+] Result {}'.format(a))


# bsort2(alist)


# alist = [6,3,5,4,2]
def short_bubble_sort(alist):
    print('\n[+] short_bubble_sort started on: {}'.format(alist))
    exchanges = True              # to catch sorted state asap
    exch_counter = 0
    passnum = len(alist)-1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchanges = True
                exch_counter += 1
                print(alist)
        passnum -= 1
    return print('[+] result: {}, total exchanges:{}'.format(alist, exch_counter))

short_bubble_sort(alist)
