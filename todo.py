from db import T
import sys

match sys.argv[1:]:
    case ['remove', i]: del T[int(i)]
    case ['list']:      print('\n'.join(f'{i}: {item}' for i, item in enumerate(T)))
    case [*args]:       T.append(' '.join(args))

open('db.py','w').write(f'T = {T}')