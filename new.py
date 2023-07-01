T = []
history = []

exec(';'.join(history))
import sys

f = open(__file__,'r+')
content = f.read().splitlines()
before, after = content[:-19], content[-19:]
f.truncate(0)
f.seek(0) 
f.writelines('\n'.join(before)+'\n')

match sys.argv[1:]:
    case ['remove', i]: f.write(f"""history += ["del T[{i}]"]\n""")
    case ['list']:      print('\n'.join(f'{i}: {item}'for i, item in enumerate(T)))
    case ['undo']:      f.write(f'history.pop()\n')
    case []:            pass
    case [*items]:      f.write(f"""history += ["T+=['{' '.join(items)}']"]\n""")

f.write('\n'.join(after))