T = []
import sys

f = open('main.py','r+')
content = f.read().splitlines()[-15:]
f.truncate(0)
f.seek(0)
f.write(f'T = []\n')

match sys.argv[1:]:
    case ['remove', i]: f.write(f'del T[{i}]\n')
    case ['list']:      print('\n'.join(f'{i}: {item}'for i, item in enumerate(T)))
    case []:            pass
    case [*items]:      f.write(f'T += [{" ".join(items)}]\n')

f.write('\n'.join(content))