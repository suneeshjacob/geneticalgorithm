def binary_range(a, b, chromosome_length = 10):
    n = 2**chromosome_length - 1
    h = (b-a)/n
    dictionary = dict([(bin(i)[2:].zfill(chromosome_length),a+i*h) for i in range(n+1)])
    return dictionary
