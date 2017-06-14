valor = input().split(" ")

a,b,c = valor
r=3.14159

triangle=(1/2)*float(a)*float(c)

radius=r*float(c)*float(c)

trap = 1/2*(float(a)+float(b))*float(c)

squ = float(b)*float(b)

rect = float(a) * float(b)

print('TRIANGULO: %.3f'%triangle)
print('CIRCULO: %.3f'%radius)
print('TRAPEZIO: %.3f'%trap)
print('QUADRADO: %.3f'%squ)
print('RETANGULO: %.3f'%rect)
