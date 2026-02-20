from simplega.simplega import GA
import itertools

def binary_range(a, b, chromosome_length = 10, string_type = 'str'):
    n = 2**chromosome_length - 1
    h = (b-a)/n
    if string_type == 'str':
        dictionary = dict([(bin(i)[2:].zfill(chromosome_length),a+i*h) for i in range(n+1)])
    elif string_type == 'bool':
        keys = list(itertools.product([True,False],repeat=3))
        values = [a+i*h for i in range(n+1)]
        dictionary = dict(zip(keys,values))
    return dictionary

# def binary_range(range_of_variable, chromosome_length = 10):
#     a, b = range_of_variable
#     n = 2**chromosome_length - 1
#     h = (b-a)/n
#     dictionary = dict([(bin(i)[2:].zfill(chromosome_length),a+i*h) for i in range(n+1)])
#     return dictionary


f = lambda x:(x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2
bounds = [(0,5),(0,5)]
n = len(bounds)

string_size = 10



def get_values_from_dna(string):
    strings = []
    cursor = 0
    for i in range(n):
        strings.append(string[cursor:cursor+string_size])
        cursor += string_size
    x_vals = [dictionaries[i][strings[i]] for i in range(len(dictionaries))]
    return x_vals

def func(chromosome_string):
    x = get_values_from_dna(chromosome_string.dna)
    fitness_value = f(x)
    return -fitness_value

def maximize(chromosome):
    return max([func(gene) for gene in chromosome.dna])

dictionaries = [binary_range(*i) for i in bounds]

ga = GA(func,chromosome_size=n*string_size,population_size=100,genes=['0','1'],generations=100000)

ga.run()

print(ga.get_fittest())
