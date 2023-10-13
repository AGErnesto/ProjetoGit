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


    4 - Operadores Aritiméticos

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
    