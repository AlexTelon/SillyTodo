T = []
import sys

match sys.argv[1:]:
    case ['remove', i]: del T[int(i)]
    case ['list']:      print('\n'.join(f'{i}: {item}'for i, item in enumerate(T)))
    case []:            pass
    case [*items]:      T += [' '.join(items)]

f = open('main.py','r+')
content = f.read().splitlines()[1:]
f.truncate(0)
f.seek(0)
f.write(f'T = {repr(T)}\n' + '\n'.join(content))