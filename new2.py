T = []
import sys

f = open(__file__,'r+')
content = f.read().splitlines()
before = content[:-19]
f.truncate(0)
f.seek(0)
op = ''

match sys.argv[1:]:
    case ['remove', i]: op = f'del T[{i}]\n'
    case ['list']:      print('\n'.join(f'{i}: {item}'for i, item in enumerate(T)))
    case ['undo']:      before = before[:-1]
    case []:            pass
    case [*items]:      op = f"T += ['{' '.join(items)}']\n"

f.write('\n'.join(before)+'\n')
f.write(op)
f.write('\n'.join(content[-19:]))