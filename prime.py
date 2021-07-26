import random

def prime(x):
    isPrime = True
    if x == 2:
        return isPrime
    
    for num in range(2, x):
        if x % num == 0:
            isPrime = False
    
    return isPrime

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(n)
    return prime_list

#1~x 사이 임의의 소수 선택
def random_choice(x):
    prime_list = primesInRange(1,x)
    randomPrime = random.choice(prime_list)
    return randomPrime