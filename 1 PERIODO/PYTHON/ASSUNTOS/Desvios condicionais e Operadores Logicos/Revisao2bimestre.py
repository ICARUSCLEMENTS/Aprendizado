

# Muitas vezes precisamos aninhar vários if para obter o comportamento desejado do programa. Aninhar, nesse caso, é utilizar um if dentro de outro.
# Planos de uma empresa de telefonia: Os planos da empresa oferecem preços diferenciados de acordo com a quantidade de minutos usados por mês.
# - Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
# - Entre 200 e 400 minutos, o preço é de R$ 0,18.
# - Acima de 400 minutos, o preço por minuto é de R$ 0,15.

minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200:

    preço = 0.20

# Python apresenta uma solução muito interessante ao problema de múltiplos ifs alinhados. A cláusula elif substitui um par else if, mas sem criar outro nível de estrutura, evitanto problemas de deslocamentos desnecessários á direita.
# Vamos refatorar a solução do problema das categorias utilizando elif.
elif minutos < 400:

   preço = 0.18

else:

    preço = 0.15

print("Você vai pagar este mês: R$%6.2f" % (minutos * preço))
