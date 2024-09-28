# Aula 38 e 39 - Parte 1 e Parte 2: Variáveis, constantes e complexidade de código
Vamos falar sobre a complexidade de códigos e algumas boas práticas.

Vamos analisar o seguinte código

    velocidade = 61  # velocidade atual do carro
    local_carro = 100  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

No caso, essa parte onde está sendo exibido duas formas de declarar as variáveis vamos avaliar se está sendo feito uma boa prática ou não.

Note que, as variáveis escritas em maiúsculas são os mesmos das que estão sendo declaradas em minúsculas.

No caso, lembremos que em python, diferentemente de JavaScript, não existe uma forma de declarar uma variável que seja constante. Ou seja, uma vez declarada ao longo do processo ela nunca poderá ser mudada. Ou seja, uma vez declarada as variáveis em maiúsculas, elas podem ser atribuídas outros valores novamente.

Bom, ciente desse fato, como vamos poder contornar a tal situação?

O que recomendamos é que se for algum valor que vc não queira que seja mudado o seu valor, que vc atribuia a sua variável de forma maiúscula, como podemos ver acima em RADAR_1, LOCAL_1 e RADAR_RANGE.

Agora, uma prática considerada ruim no âmbito de condicionais, seriam aquelas condicionais que tenha muita, mas muita, lógica booleana. No caso, em um único if vc coloca uma série de and e or. O que deixaria o seu código muito, mas muito, complexo. A princípio, isso seria uma má prática, pois tornaria a leitura do seu código muito difícil de interpretar para avaliar se uma dada condição permitiria entrar ou não naquele if.

Basicamente, a regra geral em programação, é que sejam escritos códigos que fácil interpretação. Algo que foge bem longe daqueles códigos que vc não entende nada o que está sendo escrito nos filmes de hackers.

Outra prática que é considerada ruim seria colocar códigos de blocos dentro de outros códigos de blocos. Novamente, isso entra n complexidade de código que tornaria-a muito, mas muito, complexo para a leitura e entendimento da mesma. O ideal é que vc saiba separar cada bloco em cada lugar separadamente ou até mesmo em funções para vc conseguir chamar em momentos quando é necessário.

Bom, a moral da história, seria que os códigos precisam ser, na medida do possível, o mais simples e possível e bem organizado.

Bom, ciente disso, vamos implementar as condicionais usando as variáveis dos códigos acima para colocar em prática o que seria um código de boa prática

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    if velocidade > RADAR_1:
        print('Velocidade carro passou do radar 1')
        
    if local_carro >= (LOCAL_1 + RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
            velocidade > RADAR_1:
        print('carro multado em radar 1')

Bom, note que, acima já está aparecendo uma má prática. Qual seria?

A resposta é que o comparativo velocidade > RADAR_1 já está sendo usado mais de uma vez nas condicioais.

Bom, como iremos corrigir isso?

Da seguinte forma

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    vel_carro_pass_radar_1 = velocidade > RADAR_1
    carro_multado_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

    if vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')
        
    if carro_multado_radar_1 and vel_carro_pass_radar_1:
        print('carro multado em radar 1')
    
Ou seja, as condicionais eu denotei elas como variáveis para colocar nos if's.  

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    vel_carro_pass_radar_1 = velocidade > RADAR_1
    carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

    if vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')
        
    if carro_passou_radar_1:
        print('Carro passou radar 1')
        
    if carro_multado_radar_1:
        print('carro multado em radar 1')

Aqui está a versão mais simplificada e munida de boas práticas.
