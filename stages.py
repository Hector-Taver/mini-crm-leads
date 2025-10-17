from datetime import date

STAGES = ['novo']

def lead_model(name, company, email):
  """Modela/estrutura um lead como um dicionário"""
  return {
    "name": name,
    "company": company,
    "email": email,
    "stage": "novo",
    "created_at": date.today().strftime('%Y-%m-%d %H:%M:%S')
  }
