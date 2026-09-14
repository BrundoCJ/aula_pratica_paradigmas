# Atividade - Aula 04

[← Voltar ao índice](../README.md)

Aula exploratória sobre **análise léxica e análise sintática**, baseada no
capítulo 4 de Sebesta. A prática foi dividida em cinco estações com programas
Java 17.

| Item | Informação |
|---|---|
| Aluno | Pedro Luiz Carvalho Mendes |
| RA | 24055157-2 |
| Entrega | [aula-exploratoria.pdf](aula-exploratoria.pdf) |

## Objetivo

Observar etapas que normalmente ficam ocultas em um compilador: separação de
lexemas, classificação de tokens, diagnóstico de erros e funcionamento de
analisadores descendentes e ascendentes.

## Estações

| Estação | Tema | Conceito observado |
|---:|---|---|
| 1 | Lexemas e tokens | transformação de caracteres em unidades com significado |
| 2 | Classes e palavras reservadas | diferença entre identificadores, reservadas e símbolos inválidos |
| 3 | Diagnósticos | identificação e correção de erros léxicos e sintáticos |
| 4 | Parser descendente | chamadas recursivas, precedência e *lookahead* |
| 5 | Parser ascendente | pilha e operações `SHIFT`, `REDUCE` e `ACCEPT` |

## 1. De caracteres a lexemas e tokens

O analisador recebe uma linha de código e agrupa os caracteres em lexemas. Em
seguida, associa cada lexema a uma categoria, chamada token.

Exemplo:

```text
total_PLCM = valor + 72;
```

| Lexema | Token |
|---|---|
| `total_PLCM` | `IDENTIFICADOR` |
| `=` | `ATRIBUICAO` |
| `valor` | `IDENTIFICADOR` |
| `+` | `SOMA` |
| `72` | `INTEIRO` |
| `;` | `PONTO_E_VIRGULA` |

Lexema é o texto concreto encontrado no código. Token é a categoria desse
texto. Assim, `total_PLCM` e `valor` são lexemas diferentes, mas recebem o
mesmo token.

## 2. O que o analisador léxico reconhece

Os testes da segunda estação permitem observar que:

- espaços extras não alteram a sequência essencial de tokens;
- comentários são ignorados;
- `int` é uma palavra reservada, enquanto `inteiro` é um identificador;
- um caractere não previsto, como `#`, produz um erro léxico.

A classificação de uma palavra depende da consulta à lista de reservadas, e
não apenas de suas primeiras letras.

## 3. Diagnósticos do compilador

O programa da terceira estação possui erros intencionais:

- ausência de ponto e vírgula;
- parêntese de uma condição não fechado;
- texto sem aspas de fechamento.

O texto não finalizado interfere na formação de um elemento léxico. O ponto e
vírgula e o parêntese ausentes violam a estrutura sintática esperada. Depois da
correção mecânica, o programa compila e exibe o resultado normalmente.

## 4. Parser descendente recursivo

O parser descendente começa pelo símbolo mais geral e chama métodos que
representam regras menores, como `expr`, `term` e `factor`. Na expressão:

```text
2 + 3 * 4
```

`term` reconhece a multiplicação antes de `expr` concluir a soma, resultando em
14. Com parênteses, `(2 + 3) * 4`, a soma é reconhecida dentro de `factor` e o
resultado passa a ser 20.

Uma produção com recursão à esquerda não pode ser aplicada diretamente a esse
parser: a regra chamaria a si mesma sem consumir nenhum token e entraria em
recursão infinita.

## 5. Parser ascendente

O analisador ascendente parte dos tokens e tenta reduzi-los até chegar ao
símbolo inicial da gramática.

| Ação | Significado |
|---|---|
| `SHIFT` | move o próximo item da entrada para a pilha |
| `REDUCE` | substitui itens reconhecidos pelo lado esquerdo de uma produção |
| `ACCEPT` | confirma que toda a entrada pertence à linguagem |
| `ERROR` | indica que não existe ação válida para a configuração atual |

## Comparação dos parsers

| Aspecto | Descendente | Ascendente |
|---|---|---|
| Início | símbolo inicial | tokens da entrada |
| Direção | do geral para os componentes | dos componentes para o geral |
| Mecanismo | chamadas recursivas | pilha e tabela de análise |
| Recursão à esquerda | precisa ser eliminada | pode ser tratada naturalmente |

## Evidências da prática

O PDF final deve reunir seis capturas legíveis, mostrando código e console:

- [x] entrada personalizada e seus tokens;
- [x] palavra reservada, identificador e erro léxico;
- [x] erros emitidos pelo compilador;
- [x] programa corrigido em execução;
- [x] rastreamento do parser descendente;
- [x] pilha e `ACCEPT` do parser ascendente.

As seis evidências estão reunidas nas três páginas do
[PDF da entrega](aula-exploratoria.pdf), com a identificação do aluno visível.

## Síntese

O analisador léxico converte caracteres em tokens. O analisador sintático
verifica se a sequência desses tokens obedece à gramática. Parsers descendentes
e ascendentes percorrem a estrutura em direções diferentes, mas têm o mesmo
objetivo: decidir se a entrada é sintaticamente válida.

## Referências

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11. ed.
  Capítulo 4: análise léxica e sintática.
- Roteiro da aula exploratória fornecido pelo professor.
