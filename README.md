# desafio-smarttbot

# Média móvel exponencial
O cálculo da média móvel foi baseado no livro do Flávio Lemos [1]:

O cálculo da média é iniciado com uma média aritmética simples e depois implementado utilizando a média exponencial do período imediatamente anterior, a média não é calculada para todos os elementos da série porque o primeiro elemento depende de N valores anteriores para se calculado, onde N é igual ao período da média.

MMS = soma(N)/N

fator = 2/(N + 1)

MME = (Preço - MME[anterior]) * fator + MME[anterior]

# Bandas de Bollinger
As bandas de bollinger consistem em uma média com duas outras linhas, uma superior e outra inferior em relação a média, ambas as linhas são cálculadas utilizando o desvio padrão em um período, neste caso o mesmo período utilizado para calcular a média, que se trata de uma média móvel exponencial.[2]

O desvio padrão é calculado levando em consideração os preços do ativo e não valores da média.

As bandas de bollinger clássicas utilizam 2 desvios padrões, ou seja x = 2.

Linha superior = MME + (x * desvio padrão)

Linha inferior = MME - (x * desvio padrão)

# Indice de força relativa
O Índice de força relativa (IFR) compara a magnitude dos ganhos recentes em um ativo e de suas perdas, retornando números de 0 a 100, na prática é o percentual de ganhos de touros em relação aos ursos em um determinado período.[3]

IFR = 100 - [100 / (1 + (A/B))]
A = Média de n fechamentos de alta
B = Média de n fechamentos de baixa

Fechamentos de alta acontecem quando o preço de fechamento de um candle é maior do que o de abertura e fechamentos de baixa são analogamente opostos aos de alta.

# Referências
[1] Média móvel exponencial(MME). In: LEMOS, Flávio. Análise Técnica dos Mercados Financeiros: Um Guia Completo e Definitivo dos Mercados de Negociação de Ativos. São Paulo - SP: Saraiva, 2016. cap. 8.2.3, p. 181-183

[2] Bandas de Bollinger. In: LEMOS, Flávio. Análise Técnica dos Mercados Financeiros: Um Guia Completo e Definitivo dos Mercados de Negociação de Ativos. São Paulo - SP: Saraiva, 2016. cap. 8.3.3, p. 201-206

[3] Indice de Força Relativa (IFR) ou Relative Strength Index (RSI). In: LEMOS, Flávio. Análise Técnica dos Mercados Financeiros: Um Guia Completo e Definitivo dos Mercados de Negociação de Ativos. São Paulo - SP: Saraiva, 2016. cap. 9.5.1, p. 263-269