import pandas as pd
from twilio.rest import Client

account_sid = 'ACc50f2150419ae884e59aff1e63548e03'
auth_token = '6b8fbc00d5512c8957979ad6ed85b038'
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            to='',
            from_='+16203129481',
            body=f'No mês de {mes}, alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        print(message.sid)




# Para cada arquivo:
    # Verificar se algum valor na coluna de vendas é maior do que 55.000
    # Se for maior do que 55.000 -> enviar SMS com nome, mês e as vendas do vendedor
    # Caso não seja maior do que 55.000, não fazer nada.



