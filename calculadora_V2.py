def cal(NuOpe1, NuOpe2, ope):
    if(ope == 1):
      return NuOpe1 + NuOpe2
    elif(ope == 2):
       return NuOpe1 - NuOpe2
    elif(ope == 3):
     return NuOpe1 * NuOpe2
    elif(ope == 4):
     return NuOpe1 / NuOpe2
    else:
     print("Essa operação não existe")
NuOpe1=1
while(NuOpe1 != 0):
  print("tipos de operações disponiveis")
  print("1: Soma ")
  print("2: subtração")
  print("3: multiplicação")
  print("4: divisão")
  print("0: para sair")
  print("digite o primero numero")
  NuOpe1=float(input())
  if (NuOpe1 == 0):
    print("fim do programa")
    break
  print("digite o segundo numero")
  NuOpe2=float(input())
  print("digite o numero da operação")
  ope=int(input())
  resultado=cal(NuOpe1, NuOpe2, ope)
  print("resutado : " + str(resultado))
  print(" ")