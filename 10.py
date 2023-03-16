n= int(input("Número de três digitos: "))
a= n%100
b= n//100
c= a//10
d= a%10
e= (d*100)+(c*10)+b
print(e)