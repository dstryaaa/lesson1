def get_summ(one, two, delimeter=' '):
    #return str(one) + str(delimeter) + str(two)
    return '{} {} {}'.format(one, delimeter, two)

print(get_summ(2, 2, delimeter='&'))

print(get_summ('Hello', 'World!', '+'))
