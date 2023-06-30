todo = []
import sys

args = ['main.py', 'add', 'buy', 'milk']
todo.append(' '.join(args[1:]))

# match args[1:]:
#     case ['add', *items]:
#         todo.append(' '.join(items))
#     case 'list':
#         print('\n'.join(todo))
#     case _:
#         print('Unknown command')


def save():
    with open('todo.py', 'w') as f:
        # replace first line of todo.py
        f.write('todo = ' + repr(todo) + '\n')


save()