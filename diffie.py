import math

p = int(input('p: '))
g = int(input('g: '))
print()

print('USER 1')
a = int(input('a: '))
xa = g ** a
xa = math.fmod(xa, p)
print('Xa:', xa)
print('Xa transmitted to USER 2')
print()

print('USER 2')
b = int(input('b: '))
xb = g ** b
xb = math.fmod(xb, p)
print('Xb:', xb)
print('Xb transmitted to USER 1')
print()

ka = xb ** a
ka = math.fmod(ka, p)
print('Key for USER 1:', ka)

kb = xa ** b
kb = math.fmod(kb, p)
print('Key for USER 2:', kb)