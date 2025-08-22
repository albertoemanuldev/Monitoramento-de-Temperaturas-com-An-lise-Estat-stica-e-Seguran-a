

import numpy as np

class SensorDeTemperatura:

    def __init__(self, nome_sensor: str, limite_minimo: float = 20.0, limite_maximo: float = 80.0):
 
        self.nome_sensor = nome_sensor
        self.limite_minimo = limite_minimo
        self.limite_maximo = limite_maximo
        self.leituras = []  # Lista para armazenar as temperaturas registradas
        print(f"✅ Sensor '{self.nome_sensor}' iniciado. Limites de segurança: {self.limite_minimo}°C a {self.limite_maximo}°C.")

    def adicionar_leitura(self, temperatura: float):
    
        self.leituras.append(temperatura)
        print(f"🌡️ Nova leitura para '{self.nome_sensor}': {temperatura:.1f}°C")
        self._verificar_leitura_atual(temperatura)

    def _verificar_leitura_atual(self, temperatura: float):
  
        if temperatura < self.limite_minimo:
            print(f"❄️🚨 ALERTA! Temperatura de {temperatura:.1f}°C está ABAIXO do limite de segurança de {self.limite_minimo}°C!")
        elif temperatura > self.limite_maximo:
            print(f"🔥🚨 ALERTA! Temperatura de {temperatura:.1f}°C está ACIMA do limite de segurança de {self.limite_maximo}°C!")
    
    def calcular_estatisticas(self) -> dict:
     
        if not self.leituras:
            print(f"⚠️ Aviso: Não há leituras no sensor '{self.nome_sensor}' para calcular estatísticas.")
            return None
        
        dados_np = np.array(self.leituras)
        
        stats = {
            "minimo": np.min(dados_np),
            "maximo": np.max(dados_np),
            "media": np.mean(dados_np),
            "total_leituras": len(dados_np)
        }
        return stats

    def exibir_relatorio_completo(self):
      
        print("\n" + "="*40)
        print(f"📊 Relatório Completo do Sensor: '{self.nome_sensor}'")
        print("="*40)
        
        estatisticas = self.calcular_estatisticas()
        
        if estatisticas:
            print(f"📈 Total de Leituras Registradas: {estatisticas['total_leituras']}")
            print(f"🧊 Temperatura Mínima Registrada: {estatisticas['minimo']:.1f}°C")
            print(f"🌶️ Temperatura Máxima Registrada: {estatisticas['maximo']:.1f}°C")
            print(f"⚖️ Média de Temperatura: {estatisticas['media']:.1f}°C")
        
        print("="*40 + "\n")