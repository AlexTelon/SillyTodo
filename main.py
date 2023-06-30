T = ['email john', 'buy milk', 'buy eggs']
import sys

def save():
    content = open('main.py').read().splitlines()[1:]
    with open('main.py', 'w') as f:
        f.writelines('\n'.join([f'T = {repr(T)}'] + content))

match sys.argv[1:]:
    case ['remove', i]:              del T[int(i)-1];save()
    case ['list']:                   print('\n'.join(f'{i}: {item}'for i, item in enumerate(T, start=1)))
    case ['add', *items] | [*items]: T.append(' '.join(items));save()
    case _:                          print('Unknown command')