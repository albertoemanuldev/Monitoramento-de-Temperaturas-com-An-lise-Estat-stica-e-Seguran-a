# Monitoramento de Temperatura — Atividade 3

Atividade proposta Monitoramento de Temperaturas com Análise Estatística e Segurança

## Curso: Fundamentos de Python para IA - SENAI

Este projeto simula o monitoramento de sensores de temperatura em diferentes ambientes, como servidores e freezers de vacinas. O sistema permite adicionar leituras de temperatura, verificar se estão dentro dos limites de segurança e exibir relatórios estatísticos.

## Estrutura dos Arquivos

- [`main.py`](atividade3/main.py): Arquivo principal de execução. Cria instâncias de sensores, adiciona leituras e exibe relatórios completos.
- [`sensor.py`](atividade3/sensor.py): Contém a classe [`SensorDeTemperatura`](atividade3/sensor.py), responsável por armazenar leituras, verificar limites e calcular estatísticas.
- [`requirements.txt`](atividade3/requirements.txt): Lista as dependências necessárias para rodar o projeto (neste caso, apenas `numpy`).

## Como executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt

2. Execute o comando:
    ```sh
    python main.py

Funcionalidades
# Adição de leituras de temperatura para diferentes sensores.
# Alertas automáticos caso a leitura esteja fora dos limites definidos.
# Relatório estatístico com mínimo, máximo, média e total de leituras.