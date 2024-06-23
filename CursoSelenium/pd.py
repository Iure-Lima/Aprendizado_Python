import pandas as pd
import os
diretorio_atual = os.getcwd()

# base = pd.read_csv('da.csv')
# print(base)

# pergunta = "Horario de funcionamento"

# respo = base.loc[base['Perguntas'] in pergunta, 'Respostas']
# respo = str(respo)
# respo = respo[6:]
# le = len(respo) - 30
# respo = respo[:le]

#buscando com in
# pergunta_cli = 'funcionamento'

# for pergunta in base["Perguntas"]:
#     if pergunta_cli in pergunta:
#         resposta = base.loc[base['Perguntas'] == pergunta]['Respostas']
#         print(resposta)

#buscando sem o in
# def interpret_message(message):
#         questions = pd.read_csv(r'./da.csv')
#         message = message.lower().split()

#         for word in message:
#             for question in questions["Questions"]:
#                 if word in question:
#                     answers = questions.loc[questions["Questions"] == question,"Answers"].index
#         try:
#             return questions.loc[answers[0]]['Answers']
#         except:
#             return False

# mesa = 'Estou com problema'
# answe = interpret_message(mesa)
# print(answe)

dados = {'Nome': ['João', 'Maria', 'José'],'Idade': [25, 30, 28]}
df = pd.DataFrame(dados)

nome_arquivo_excel = os.path.join(diretorio_atual, 'criandoPlanilha.xlsx')
nome_arquivo_csv = os.path.join(diretorio_atual, 'criandoPlanilhaCSV.csv')

df.to_excel(nome_arquivo_excel, index=False)
df.to_csv(nome_arquivo_csv, index=False)



