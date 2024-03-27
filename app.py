import os 

print ("""sabor expreess""")

print ('1. cadastrar restaurante')
print ('2. listar restaurante')
print ('3. ativar restaurante')
print ('4 sair')

opcao_escolhida = int (input ('escolha uma opção'))
#print ('vocẽ escolheu a opção', opção escolhida)
#print(f' vocẽ escolheu a opção { opção_ecolhida}')

def finalizada_app (): 
  os.system ('cls')
print ('encerrando o progama\n')

if opcao_escolhida == 1: 
 print ('cadastrar restaurante')
elif opcao_escolhida == 2:
 print (' listar restaurantes')
elif opcao_escolhida == 3:
 print ('ativar restaurante')
else:
   finalizada_app()
   