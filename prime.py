def is_prime():

    prime = [2,3,5,7,11]  

    for num in range(1000):
        if num == 1:
            continue
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            continue
        prime.append(num)
    return prime
            
            
is_prime()