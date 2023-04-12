"""
Ler tabela excel, para identificar vendedor que bateu a meta.
"""
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
ACCOUNT_SID = "AC086b7e411ae240a507da220c665c2ce7"
# Your Auth Token from twilio.com/console
AUTH_TOKEN  = "61bd4ed80fb1e9e2eae9b736f51ffee2"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        message = client.messages.create(
            to="+351910763048",
            from_="+19124935999",
            body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)
