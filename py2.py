from random import randint
lttrs_in_pool = int(randint(1000,3001))
while lttrs_in_pool in range(2500,3001):
    print('pool is full')
    break
    #Control water levels of my pool
if lttrs_in_pool in range(1500,2500):
        print('pool is half full')
        lttrs_in_pool += 1

    #fill pool 
elif lttrs_in_pool in range(0,1500):
        print("Dont use the pool till its full")
        lttrs_in_pool += 10

    #fill pool
else:
        pass