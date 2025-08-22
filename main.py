

from sensor import SensorDeTemperatura

def main():
   
    
    monitor_servidor = SensorDeTemperatura("Servidor Principal")
    
    monitor_servidor.adicionar_leitura(25.5)
    monitor_servidor.adicionar_leitura(32.0)
    monitor_servidor.adicionar_leitura(55.8)
    monitor_servidor.adicionar_leitura(85.2)  
    monitor_servidor.adicionar_leitura(18.9)  
    monitor_servidor.adicionar_leitura(45.1)

    monitor_servidor.exibir_relatorio_completo()

    monitor_freezer = SensorDeTemperatura(
        nome_sensor="Freezer de Vacinas",
        limite_minimo=-8.0,
        limite_maximo=-2.0
    )

    monitor_freezer.adicionar_leitura(-5.5)
    monitor_freezer.adicionar_leitura(-6.8)
    monitor_freezer.adicionar_leitura(-1.5)  
    monitor_freezer.adicionar_leitura(-7.2)
    
    monitor_freezer.exibir_relatorio_completo()

if __name__ == "__main__":
    main()