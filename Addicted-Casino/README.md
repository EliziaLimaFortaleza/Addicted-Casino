 # Addicted-Cassino

 A Casino game that's addicted to multiples of three

 Teacher's proposal:

 Tema: O cassino
 
Um dos jogos disponíveis num cassino é um jogo de apostas. O jogador não aposta dinheiro; em vez disso, aposta fichas. Cada jogo tem um “ganho”. Por exemplo, se o jogador apostou 20 fichas e o jogo tem um ganho de 5, se ganhar a aposta recebe 100 fichas, senão não recebe nada. Em ambos os casos, o valor apostado não é devolvido. O problema é que os jogos deste cassino estão viciados. Tipicamente, um jogo tem um ganho de n ao fim de k apostas. Por exemplo, um jogo tem ganho 2 de 3 em 3 jogadas, mas fora disso tem ganho zero. Isto quer dizer que as jogadas 3, 6, 9, ... dão ganho 2 e todas as outras tem ganho zero. Em geral, os jogadores do cassino apostam mais quando estão a ganhar e menos quando acabaram de perder uma aposta. Assuma que aquilo que o jogador aposta a mais quando ganha é igual ao que aposta a menos quando perde. O jogo termina ao fim de um número de jogadas ou caso o valor da aposta chegue a zero. Pretende-se desenvolver um programa para determinar o saldo final do jogador (em número de fichas).

 

Dados de entrada (a pedir ao utilizador):

•numfichas – número de fichas que o jogador dispõe inicialmente (p.ex. 100)

•aposta – valor da primeira aposta (em fichas, p.ex. 10)

•num-apostas – número de apostas a realizar (p.ex. 20)

•delta – valor a somar ou a subtrair à aposta, conforme o jogador ganhe ou perca a aposta anterior (p.ex. 3)

•k – número de jogadas até o jogo dar ganho (p.ex. 3)

•n – ganho do jogo de k em k jogadas (p.ex. 2)

 

Dados de saída (a apresentar no ecrã):

•o número de fichas no final do jogo (para os valores acima especificados dá 72)

 

Exigências:

a)Implemente uma função que dá o ganho do jogo para uma certa jogada, indicada pelo número da jogada.

b)Implemente uma função que devolve o número de fichas do jogador ao fim de uma jogada, indicada pelo seu número. Utilize a função anterior.

c)Escreva o programa que calcula o número de fichas com que fica o jogador no final. Utilize as funções anteriores.

 
