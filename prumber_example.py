from sympy.ntheory import factorint
import numpy as np

# Primes under N courtesy https://prime-numbers.info/list/first-100-primes.
primes = np.asarray([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                     59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                     131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                     197, 199, 211, 223, 227, 229, 233, 239, 241, 251])

def to_prumber(decimal_number):

    p = np.zeros(len(primes)).astype('int')
    for key, value in factorint(decimal_number).items():
        p[int(np.argmin(np.abs(primes-key)))] = int(value)
    return p


def to_number(primal_number):

    n = 1
    for count, k in enumerate(primal_number):
        n *= np.power(primes[count], k)
    return n


def ps(p): return ''.join([str(x) for x in p])


# Briefly check if the conversions work properly in the expected range.
# (For 2-256, max value of a 'digit' is 7, max number of non-zeros 'digits' is 4)
for v in range(2, 256): assert(v==to_number(to_prumber(v)))

a = np.random.randint(2, 256)
b = np.random.randint(2, 256)

print(f'prumber({a})\n\t= {ps(to_prumber(a))}')
print(f'prumber({b})\n\t= {ps(to_prumber(b))}')
print(f'prumber({a}*{b})\n\t= {ps(to_prumber(a*b))}')
print(f'prumber({a})+prumber({b})\n\t= {ps(to_prumber(a)+to_prumber(b))}')
print('Are the above two equal? (e.g. pr(a)+pr(b) == pr(a*b))?')
print('\t', np.all(to_prumber(a*b) == (to_prumber(a) + to_prumber(b))))