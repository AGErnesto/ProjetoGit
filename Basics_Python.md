Fundamentos:

1 - Identação em Python é considerada para bloco de códigos

```python
if 5 > 2:
    print ("5 é maior que 2")
```
Sem a identação no código acima, Python vai apresentar um erro por não conseguir interpretar o bloco de códigos.

2 - Comentários

    2.1 - Comentários em uma linha são feitos usando #:
        #comentario em uma linha
    2.2 - Comentários em multiplas linhas são feitas usando 3 aspas duplas:
        """ comentário 
            em 
            varias
            linhas"""

3 - Variáveis
    
    Não existe comando para se declarar variáveis, elas são criadas no momento em que são chamadas.
    Todas as variáveis são objetos
    Regras:
        O nome da variavel deve começar com uma letra ou "_"
        O nome da variável não pode começar com um número
        O nome da variávels não pode ter caracteres especiais, exceto o "_"
        O nome da variavel é sensível a maiúsculas e minúsculas


4 - Operadores 

    4.1 Aritiméticos

        ```python
        #Soma
            assert 2 + 2 == 4    
        
        #Subtração
            assert 5 - 2 == 3
        
        #Multiplicação
            assert 2 * 3 == 6
        
        #Divisão (resultado será sempre ponto flutuante)
            assert 5 / 3 == 1.6666666666667
            assert 2 / 2 == 1
        
        #Módulo
            assert 5 % 3 == 2

        #Exponencial
            assert 5 ** 3 == 125

        #Divisão (resultado inteiro)
            assert 5 // 3 == 1
        ```

    4.2 Operadores de Bit

        ```python
        # & - E
        # Coloca o bit em 1 se ambos os bits forem 1
        # Exemplo
        # 5 = 0b0101
        # 3 = 0b0011
        assert 5 & 3 = 1 # 0b0001

        # | - OU
        # Set o bit em 1 se um dos dois for 1
        # Exemplo
        # 5 = 0b0101
        # 3 = 0b0011
        assert 5 | 3 == 7 # 0b0111

        # ~ - NÃO
        # Inverte todos os bit
        assert ~5 == -6

        # ^ - XOR
        # Seta o bit em 1 se  somente 1 dos bits for 1
        # Exemplo
        # 5 = 0b0101
        # 3 = 0b0011
        number = 5 # 0b0101
        number ^= 3 #
        assert 5 ^ 3 == 6 # 0b0110

        # >> - Mudança para a direita
        # Empurra os bit para a direita
        # Exemplo
        # 5 = 0b0101
        assert 5 >> 1 == 2 # 0b0010
        assert 5 >> 2 == 1 # 0b0001

        # << - Mudança para a esquerda
        # Empurra os bits para a esquerda preenchendo com zero
        # Exemplo
        # 5 = 0b0101
        assert 5 << 1 == 10 # 0b1010
        assert 5 << 2 == 20 # 0b10100  
        ```

    4.3 - Operadores de Atribuição e aritméticos

        ```python
        def test_op_atribuicao ():
            """ Operador de Atribuição """

            #Atribuição
            number = 5
            assert number == 5

            #Atribuição Múltipla
            variavel_um, variavel_dois = 0, 1
            assert variavel_um == 0
            assert variavel_dois == 1

                #Da pra trocar os valores através da atribuição multipla
                variavel_um, variavel_dois = variavel_dois, variavel_um
                assert variavel_um == 1
                assert variavel_dois == 0

            def operadores_aritimeticos_bit_e_atribuicao ():
                #Atribuição e soma
                number = 5
                number += 3
                assert number == 8

                #Atribuição e subtração
                number = 5
                number -= 3
                assert number == 2

                #Atribuição e Multiplicação
                number = 5
                number *= 3
                assert number == 15

                #Atribuição e divisão
                number = 8
                number /= 4
                assert number == 2

                #Atribuição e resto
                #Retorna o resto da divisão
                number = 8
                number %= 3
                assert number == 2       
        ```