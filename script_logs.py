import csv
from datetime import datetime
import random

arquivo_logs = "logs_saida.csv"

eventos = [
    ("LOGIN_INVALIDO", "Tentativa de login inválida detectada"),
    ("EXECUCAO_SUSPEITA", "Execução de comando não autorizado"),
    ("ALTERACAO_ARQUIVO", "Arquivo crítico modificado"),
    ("ACESSO_PERMITIDO", "Login realizado com sucesso"),
    ("SERVICO_INICIADO", "Serviço do sistema iniciado")
]

def gerar_evento():
    evento = random.choice(eventos)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [data, evento[0], evento[1]]

def registrar_logs(quantidade=5):
    with open(arquivo_logs, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        if arquivo.tell() == 0:
            writer.writerow(["Data/Hora", "Tipo de Evento", "Descrição"])
        for _ in range(quantidade):
            writer.writerow(gerar_evento())
    print("Logs gerados com sucesso!")

if __name__ == "__main__":
    registrar_logs()
