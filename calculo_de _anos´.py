caracter_certo=True
while(caracter_certo == True) :
 try:
  nome=input("escerva o seu nome :")
  ano=int(input("escreva o ano de seu nacimento :"))lix
  if (ano < 1922 or ano > 2021):
   print("Ano invalido")
   print("Tente novamente")
   continue
  else:
   print(str(2021-ano))
   break
 except:
  print("Caracter invalido")
  print("Tente novamente")
  


