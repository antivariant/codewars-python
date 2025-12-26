import math

def divisors(n):
    divs= set()
    for i in range(1, math.isqrt(n)+1):
        if n%i==0:
            divs.add(i)
            m=n//i
            if m!=i:
                divs.add(m)
    return len(divs)
    
