import requests
import json

def cambio_acoes():
    url = "https://api.hgbrasil.com/finance?key=SUA-CHAVE"

    requisicao = requests.get(url)
    cotacoes = requisicao.json()

    # Moedas
    dolar_atual = cotacoes['results']['currencies']['USD']['buy']
    dolar_variacao = cotacoes['results']['currencies']['USD']['variation']

    euro_atual = cotacoes['results']['currencies']['EUR']['buy']
    euro_variacao = cotacoes['results']['currencies']['EUR']['variation']


    # Ações
    ibovespa = cotacoes['results']['stocks']['IBOVESPA']['variation']
    nasdaq = cotacoes['results']['stocks']['NASDAQ']['variation']


    return {
        'dolar_atual': dolar_atual,
        'dolar_variacao': dolar_variacao,
        'euro_atual': euro_atual,
        'euro_variacao':euro_variacao,
        'ibovespa':ibovespa,
        'nasdaq':nasdaq,
    }