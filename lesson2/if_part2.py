def type_definition(one, two):
    if one is not str(one) and two is not str(two):
        print('0')
    elif one == two:
        print('1')
    elif len(one) > len(two):
        print('2')
    elif one != two and two is str('learn'):
        print('3')
        

#когда будет ответ "0"
type_definition(1, 3)

#когда будет ответ "1"
type_definition('cat', 'cat')

#когда будет ответ "2"
type_definition('book', 'cat')

# когда будет ответ "3"
type_definition('book', 'learn')
