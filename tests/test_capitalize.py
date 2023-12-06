from capitalize import capitalize


# PHASE-1 (tests writteen via 'if' and 'exception')
# if capitalize('hello') != 'Hello':
    # raise Exception('Функция работает неверно!')

# if capitalize('') != '':
    # raise Exception('Функция работает неверно!')


# PHASE-2 (tests written via 'assert')
assert capitalize('hello') == 'Hello'
assert capitalize('') == ''


print('Все тесты пройдены!')
