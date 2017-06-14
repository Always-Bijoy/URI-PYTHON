import math

valor = input().split(" ")
a,b,c = valor

major = (int(a) + int(b) + abs(int(a)-int(b)))/2
total = (int(major)+ int(c) +abs(int(major)- int(c)))/2

print("%d eh o maior" %total)
