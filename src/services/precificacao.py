import random
import pandas as pd
from src.data import get_lista_medicamentos

class ServicoCotacao:
    def __init__(self):
        self.dados_brutos = get_lista_medicamentos()

    def _simular_variacao(self, preco_base):
        """Regra de Negócio: Simula variação de preço entre concorrentes."""
        farma_a = round(preco_base * random.uniform(0.95, 1.05), 2)
        farma_b = round(preco_base * random.uniform(0.90, 1.15), 2)
        farma_c = round(preco_base * random.uniform(1.00, 1.20), 2)
        
        melhor_preco = min(farma_a, farma_b, farma_c)
        economia = max(farma_a, farma_b, farma_c) - melhor_preco
        
        return farma_a, farma_b, farma_c, melhor_preco, economia

    def gerar_dataframe_atualizado(self):
        """Processa a lista e retorna o DataFrame pronto para uso."""
        lista_final = []
        for item in self.dados_brutos:
            p_a, p_b, p_c, melhor, econ = self._simular_variacao(item["Preco_Base"])
            lista_final.append({
                "Medicamento": item["Medicamento"],
                "Marca Ref.": item["Ref"],
                "Uso Principal": item["Uso"],
                "Farma A": p_a,
                "Farma B": p_b,
                "Farma C": p_c,
                "Melhor Preço": melhor,
                "Economia": econ
            })
        return pd.DataFrame(lista_final)