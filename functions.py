def binary_range(a, b, chromosome_length = 10):
    n = 2**chromosome_length - 1
    h = (b-a)/n
    dictionary = dict([(bin(i+1)[2:].zfill(chromosome_length),i*h) for i in range(n)])
    return dictionary

