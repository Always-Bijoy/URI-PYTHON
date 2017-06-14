prod1,unprod1,price= input().split()
prod2,unprod2,price2= input().split()

sum=(int(unprod1)*float(price))+(int(unprod2)*float(price2))

print("VALOR A PAGAR: R$ %.2f"%sum)
