import os
from tqdm import tqdm
print("""
                       #####   #####   ######   ######   ######    ########    ######
                       #       #       #   ##   #    #   #     #   #      #    #   ##
                       #  ##   #####   # ##     ######   #     #   #      #    #  #
                       #   #   #       #   #    #    #   #     #   #      #    #   #
                       #####   #####   #    #   #    #   ######    ########    #    #
                                       DE NÚMEROS TELEFÔNICOS
                                ====================================
                                @ Site: www.gustahtocantins.com.br @
                                @    Instagram: @gustahtocantins   @
                                ====================================
""")
def checar(numero):
   d=0
   try:
      numero[2]
      d += 1
   except IndexError:
      pass
   try:
      numero[1]
   except IndexError:
      d +=1
   if(d != 0):
      return False
   else:
      return True

while True:
   estado = input("> Código do Estado: ")
   num = input("> Código da operadora: ")
   if(checar(num)):
      if("GerarNumero" in os.listdir()): 
         pass
      else:
         os.mkdir("GerarNumero")
      arq = open(f"GerarNumero/{num}.txt","w")
      n = int(f"9{int(num)}000000")
      for x in tqdm(range(1000000)):
         arq.write(f"+55{estado}{n}\n")
         n += 1
      arq.close()
   else:
      print("Você precisa adicionar dois digitos")

   print("Realizado com sucesso!")
