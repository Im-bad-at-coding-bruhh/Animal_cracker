from random import shuffle

def is_sorted(lst):
    return lst == sorted(lst)

def bogo_sort(lst):
    m = 0
    while not is_sorted(lst):
        shuffle(lst)
        m += 1
    print(f'Done, no of iterations = {m}')

g = [0,4,5,6,7,8,9,3,2,1]
bogo_sort(g)