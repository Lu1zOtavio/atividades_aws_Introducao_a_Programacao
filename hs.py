def ve_ele(arr):
  achou = False
  while achou  == False:
    nomeachar=input("escolha o nome")
    for l in range(len(arr)):
     if arr[l] == nomeachar:
      achou = True
    if (achou == False):
      print("não achei o elemento " + nomeachar)
    else:
      print("achei o nome :" + nomeachar)
#lista_frutas.pop()
#arr.append()
#len()

nomes = ["rafael", "luiz", "lois", "luiza"]
ve_ele(nomes)
