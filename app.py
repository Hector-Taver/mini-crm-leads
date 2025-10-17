from stages import lead_model
import repo

def add_lead():
  name = input('Nome: ')
  company = input('Empresa: ')
  email = input('E-mail: ')

  repo.create_lead(lead_model(name, company, email))

  print('Lead adicionado')

def list_leads():
    leads = repo.read_leads()

    if not leads:
        print('Nenhum lead cadastrado')
        return

    print(f'\n## | {'Nome':<20} | {'Empresa':<20} | {'E-mail':<20}')
    for i, lead in enumerate(leads):
      print(f'{i:02d} | {lead['name']:<20} | {lead['company']:<20} | {lead['email']:<20}')

def search_leads():
  user_seach = input('Buscar por: ').strip().lower()
  if not user_seach:
    print("Busca vazia")
    search_leads()

  leads = repo.read_leads()
  results = []

  for lead in leads:
    lead_str = f'{lead['name']} {lead['company']} {lead['email']}'.lower()
    if user_seach in lead_str:
      results.append(lead)

  if not results:
    print('Nenhum lead encontrado')
    return

  print(f'\n## | {'Nome':<20} | {'Empresa':<20} | {'E-mail':<20}')
  for i, result in enumerate(results):
    print(f'{i:02d} | {result['name']:<20} | {result['company']:<20} | {result['email']:<20}')


def export_leads():
  path_csv = repo.export_csv()
  if path_csv is None:
    print('Erro ao exportar o CSV... tente fechar o arquivo')
  else:
    print(f'CSV exportado para {path_csv}')

def main():
  while True:
    print_menu()
    op = input('Escolha: ')

    if op == '1':
      add_lead()
    elif op == '2':
      list_leads()
    elif op == '3':
      search_leads()
    elif op == '4':
      export_leads()
    elif op == '0':
      print('Até logo!')
      break
    else:
      print('Opção inválida')

def print_menu():
  print('\nMini CRM de Leads - (Adicionar/Listar)')
  print('[1] Adicionar Lead')
  print('[2] Listar Lead')
  print('[3] Buscar leads por (nome/empresa/email)')
  print('[4] Exportar leads como CSV')
  print('[0] Sair')

if __name__ == '__main__':
  main()
