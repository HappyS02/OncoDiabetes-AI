# 6- Agent & 7- Agent AI (Otonom görevler)

class HealthAgent:
    def __init__(self, role, task):
        self.role = role
        self.task = task

    def execute(self, val):
        return f"[{self.role}] Aksiyon: {self.task} (Değer: {val})"

# 6. Agent & 7. Agent AI
diet_agent = HealthAgent("Diyetisyen", "Karbonhidrat kısıtlaması uygula")
doc_agent = HealthAgent("Onkoloji Uzmanı", "Acil kontrol randevusu oluştur")

def coordinate_agents(risk_score, glucose):
    if risk_score > 0.6:
        return f"{diet_agent.execute('Sıkı Plan')}\n{doc_agent.execute(glucose)}"
    return "Durum stabil, rutin takibe devam."