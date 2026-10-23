# Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

def is_prime(n):
    for i in range(2,n+1):
        if (n%i==0):
            i+=1
            
is_prime(12)