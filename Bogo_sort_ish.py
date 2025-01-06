from random import shuffle

def is_sorted(lst):
    return lst == sorted(lst)

def bogo_sort(lst):
    m = 0
    while not is_sorted(lst):
        shuffle(lst)
        m += 1
    print(f'Done, no of iterations = {m}')

g = [5,2,7,4,4,3,2,1]
bogo_sort(g)