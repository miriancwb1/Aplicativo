import os
restaurantes = [{'nome': 'pizza xp','caategoria' : 'alimento', 'ativo' : False},
                {'nome' : 'santa', 'categoria': 'alimento', 'ativo' : False},
                {'nome' : 'CWB', 'categoria': 'pizza ', 'ativo': False }]
        


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

def opcao_invalida():
 print ('opção invalida!\n')
 voltar_ao_menu_principal()


def listar_restaurante():
  exibir_subtitulos ('listando os restaurantes')

  for restaurantes in restaurantes:
    print (f'*{restaurantes}')


def exibir_subtitulos (texto):
  os.system ('clear')
  linha = '*' * (len(texto))
  print (linha)
  print (texto)
  print (linha)
  print ()


def cadastar_novo_restaurante():
    exibir_subtitulos ('cadastros de novos restaurante:')
    nome_do_restaurante = input ('digite o nome do novo restaurante')
    categoria = input (f'digite a categoria do restaurante' {nome_do_restaurante}:)
    dado_do_restaurante = {' nome': nome_do_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append (dado_do_restaurante)
    print (f'o restaurante  {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal
    


def listar_restaurante ():
  exibir_subtitulos ('litando os restaurantes')



print (f'{"nome do restaurante"}.just (22)] | status)')
      for restaurantes in restaurantes:
      nome_do_restaurante = restaurantes ['categoria']
      ativo = 'ativado' if 



#falta terminar o lista_restaurante


def escolher_opcoes():
 try:

  opcao_escolhida = int (input ('escolha uma opção'))

  if opcao_escolhida == 1:   
   cadastar_novo_restaurante
  elif opcao_escolhida == 2:
   listar_restaurante()
  elif opcao_escolhida == 3:
   print ('ativar restaurante')
  elif opcao_escolhida == 4:
    finalizada_app
  else:
    opcao_escolhida
 except:
   opcao_invalida()
    
def main(): 
  os.system('cls')
  exibir_nome_do_progama()
  exibir_opcaoes()
  escolher_opcoes()


  if __name__=='__main__':
    main()
