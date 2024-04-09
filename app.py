import os
restaurantes = {'pizza,xp'} #lista de restaurantes

def exibir_nome_do_progama ():
 print ("""sabor expreess""")
def exibir_opcaoes():
 print ('1. cadastrar restaurante')
 print ('2. listar restaurante')
 print ('3. ativar restaurante')
 print ('4 sair')

def finalizada_app (): 
 exibir_subtitulos ('finalizar app') 

def voltar_ao_menu_principal():
   input ('\n digite a tecla "enter" para voltar ao menu principal')
   main()


opcao_escolhida = int (input ('escolha uma opção'))
#print ('vocẽ escolheu a opção', opção escolhida)
#print(f' vocẽ escolheu a opção { opção_ecolhida}')

def exibir_subtitulos (texto):
  os.system ('clear')
  print (texto)
  print ()

if opcao_escolhida == 1: 
 def escolher_opcoes():
  print ('cadastrar restaurante')
elif opcao_escolhida == 2:
 print (' listar restaurantes')
elif opcao_escolhida == 3:
 print ('ativar restaurante')
else:
   finalizada_app()
  
def main(): 
  os.system('cls')
  exibir_nome_do_progama()
  exibir_opcaoes()
  escolher_opcoes()


  if __name__=='__main__':
    main()