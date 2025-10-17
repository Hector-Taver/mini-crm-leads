from stages import lead_model
import repo

def add_lead():
  name = input('Nome: ')
  company = input('Empresa: ')
  email = input('E-mail: ')

  repo.create_lead(lead_model(name, company, email))

  print('Lead adicionado')

def list_leads():
    print('Listar leads')

def main():
  while True:
    print_menu()
    op = input('Escolha: ')

    if op == '1':
      add_lead()
    elif op == '2':
      list_leads()
    elif op == '0':
      print('Até logo!')
      break
    else:
      print('Opção inválida')



def print_menu():
  print('\nMini CRM de Leads - (Adicionar/Listar)')
  print('[1] Adicionar Lead')
  print('[2] Listar Lead')
  print('[0] Sair')


if __name__ == '__main__':
  main()
