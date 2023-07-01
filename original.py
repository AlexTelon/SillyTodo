T = []
import sys

match sys.argv[1:]:
    case ['remove', i]: del T[int(i)]
    case ['list']:      print('\n'.join(f'{i}: {item}'for i, item in enumerate(T)))
    case [*items]:      T += [' '.join(items)]

content = open(__file__).read().splitlines()[1:]
with open(__file__, 'w') as f:
    f.write('\n'.join([f'T = {repr(T)}'] + content))