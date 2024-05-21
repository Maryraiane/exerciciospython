A = int(input("digite o valor de A"))
B = int(input("digite o valor de B"))
C = int(input("digite o valor de C"))

delta=B**2-4*A*C
if delta >=0 :
  print("delta",delta)
  raiz_delta=delta**0.5
  r1=(B+raiz_delta)/(2*A)
  r2 = (B-raiz_delta)/(2*A)
  print("r1")
  print("r2") 
else:
  print("impossivel calcular delta negativo")
