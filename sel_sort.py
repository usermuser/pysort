
'''
Используя линейный поиск, находим минимальное значение в последовательности.
Найденный элемент меняется местами с крайним левым элементом и после этого считается отсортированным
Если минимальное значение уже находится в крайней левой позиции, то обмен не требуется
Операция повторяется до тех пор, пока все числа не будут полностью отсортированы.

6,1,7,8,9,3,5,4,2
1,6,7,8,9,3,5,4,2

list.index(x, [start [, end]])
print(alist.index(8, 0, 4))
ValueError if not in range
Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
'''
alist = [6,1,7,8,9,3,5,4,2]
alist2 = [6,7,8,9,3,5,4,2]

tmp = ''
for i in range(len(alist)):
    pass

def get_min(lst, ins_pos):
    # get minimal number in list and its position
    min_num = lst[ins_pos]
    for i in range(ins_pos,len(lst)):
        if min_num > lst[i]:
            min_num = lst[i]

    return min_num, lst.index(min_num)

def sel_sort(lst):

    for i in lst:
        ins_pos = lst.index(i)
        min_num, min_num_pos = get_min(lst, ins_pos)
        if lst[ins_pos] == min_num:
            pass
        else:
            tmp = lst[ins_pos]
            lst[ins_pos] = lst[min_num_pos]
            lst[min_num_pos] = tmp

    return lst

result = sel_sort(alist)
print('restult = ',result)




