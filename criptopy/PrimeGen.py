import random
def PrimeGet():
    with open("primes.txt")as f:
        primi=f.read()
    primi=primi.split(" ")
    return(random.choice(primi))
print(PrimeGet())