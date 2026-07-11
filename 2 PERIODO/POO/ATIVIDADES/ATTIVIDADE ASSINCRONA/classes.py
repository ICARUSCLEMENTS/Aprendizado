class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
        self.valor_bonus = 0
    
    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas >= meta:
            return f"{self.nome} bateu a meta!"
        else:
            return f"{self.nome} não bateu a meta." 
    
    def bonus(self, meta):
        if self.vendas >= meta:
            self.valor_bonus = self.vendas * 0.1
            return f"Bônus: {self.valor_bonus:.0f}"
        return "Bônus: 0"
