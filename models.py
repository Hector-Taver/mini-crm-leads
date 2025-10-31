from datetime import date

class Lead:
  def __init__(self, name, company, email, stage):
    self.name = name
    self.company = company
    self.email = email
    self.stage = stage
    self.created_at = date.today().strftime('%Y-%m-%d %H:%M:%S')

  def lead_model(self):
    """Modela/estrutura um lead como um dicionário"""
    return {
      "name": self.name,
      "company": self.company,
      "email": self.email,
      "stage": self.stage,
      "created_at": self.created_at
    }



