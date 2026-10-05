import math
import random
import sys 
print(f'{sys.version}\n  {sys.executable},\n {len(sys.path)}')

for i in sys.path[:4]:
    print(i)

print(math.pi)
print(random.random())

print(len(sys.modules))

print(len(sorted(sys.modules)))
for j in sorted(sys.modules)[:5]:
   print(j)

public = [n for n in dir(math) if not n.startswith("_")]
print(len(public))
print(public[:8])

print("moi __name__", __name__)
print("moi __file__", __file__)

