# desafio-smarttbot

# Média móvel exponencial
O cálculo da média móvel foi baseado no livro do Flávio Lemos [1]:

O cálculo da média é iniciado com uma média aritmética simples e depois implementado utilizando a média exponencial do período imediatamente anterior, a média não é calculada para todos os elementos da série porque o primeiro elemento depende de N valores anteriores para se calculado, onde N é igual ao período da média.

MMS = soma(N)/N

fator = 2/(N + 1)

MME = (Preço - MME[anterior]) * fator + MME[anterior]

# Referências
[1] Média móvel exponencial(MME). In: LEMOS, Flávio. Análise Técnica dos Mercados Financeiros: Um Guia Completo e Definitivo dos Mercados de Negociação de Ativos. São Paulo - SP: Saraiva, 2016. cap. 8.2.3, p. 181-183