# Atividade - Aula 03

[← Voltar ao índice](../README.md)

Atividade sobre descrição de sintaxe por gramáticas. O exemplo escolhido é a
atribuição Python:

```python
total = 2 + 3 * 4
```

## 1. Fonte e tipo da gramática

A referência utilizada é a [gramática completa do Python](https://docs.python.org/3/reference/grammar.html),
escrita como uma **PEG** (*Parsing Expression Grammar*). Ela descreve como o
analisador sintático do CPython reconhece uma sequência de tokens.

A gramática léxica reconhece caracteres e forma tokens como `NAME`, `NUMBER` e
os operadores. A gramática sintática combina esses tokens em comandos,
atribuições e expressões.

### Símbolos usados

| Notação | Significado |
|---|---|
| `A B` | sequência |
| `A \| B` | escolha ordenada |
| `[A]` ou `A?` | elemento opcional |
| `A*` | zero ou mais repetições |
| `A+` | uma ou mais repetições |
| `!A` | teste negativo sem consumir entrada |

## 2. Produções selecionadas

As regras oficiais são extensas. Abaixo está somente o caminho necessário para
reconhecer o exemplo, preservando os nomes relevantes da gramática:

```text
file             -> statements ENDMARKER
statements       -> statement+
statement        -> simple_stmts
simple_stmts     -> simple_stmt NEWLINE
simple_stmt      -> assignment
assignment       -> star_targets '=' annotated_rhs
star_targets     -> star_target
star_target      -> target_with_star_atom
target_with_star_atom -> NAME
annotated_rhs    -> expressions
expressions      -> expression
expression       -> disjunction
disjunction      -> conjunction
conjunction      -> inversion
inversion        -> comparison
comparison       -> bitwise_or
bitwise_or       -> bitwise_xor
bitwise_xor      -> bitwise_and
bitwise_and      -> shift_expr
shift_expr       -> sum
sum              -> sum '+' term | term
term             -> term '*' factor | factor
factor           -> power
power            -> await_primary
await_primary    -> primary
primary          -> atom
atom             -> NUMBER
```

Algumas regras intermediárias possuem outras alternativas na gramática real.
Elas foram omitidas porque não participam deste código.

## 3. Tokens da entrada

Antes da análise sintática, o analisador léxico produz esta sequência:

```text
NAME('total') '=' NUMBER('2') '+' NUMBER('3') '*'
NUMBER('4') NEWLINE ENDMARKER
```

Espaços separam elementos, mas não aparecem como tokens nessa linha. `total` é
um lexema classificado como `NAME`; `2`, `3` e `4` são classificados como
`NUMBER`.

## 4. Derivação

Primeiro, o arquivo chega a uma atribuição:

```text
file
⇒ statements ENDMARKER
⇒ statement ENDMARKER
⇒ simple_stmts ENDMARKER
⇒ simple_stmt NEWLINE ENDMARKER
⇒ assignment NEWLINE ENDMARKER
⇒ star_targets '=' annotated_rhs NEWLINE ENDMARKER
⇒ NAME '=' expressions NEWLINE ENDMARKER
```

No lado direito, as regras de expressão descem até `sum`. A soma se divide em
um `sum`, o operador `+` e um `term`:

```text
expressions
⇒ expression
⇒ ...
⇒ sum
⇒ sum '+' term
⇒ term '+' term
```

O `term` da esquerda chega ao número `2`. O `term` da direita usa sua
alternativa de multiplicação:

```text
term '+' term
⇒ factor '+' term '*' factor
⇒ NUMBER('2') '+' factor '*' factor
⇒ NUMBER('2') '+' NUMBER('3') '*' NUMBER('4')
```

Reunindo alvo, operador e expressão:

```text
NAME('total') '=' NUMBER('2') '+' NUMBER('3') '*'
NUMBER('4') NEWLINE ENDMARKER
```

Essa é exatamente a sequência de tokens do programa.

## 5. Árvore sintática simplificada

```text
file
└── assignment
    ├── alvo: NAME("total")
    ├── '='
    └── sum
        ├── NUMBER(2)
        ├── '+'
        └── term
            ├── NUMBER(3)
            ├── '*'
            └── NUMBER(4)
```

A multiplicação está em um nó mais profundo que a soma. Isso representa a
precedência: primeiro é calculado `3 * 4`, depois `2 + 12`. O valor atribuído a
`total` é, portanto, **14**.

## 6. Terminais e não terminais

### Terminais

Os terminais efetivamente consumidos são `NAME`, `'='`, `NUMBER`, `'+'`, `'*'`,
`NEWLINE` e `ENDMARKER`. `NAME` e `NUMBER` são categorias produzidas pelo
analisador léxico.

### Não terminais

Os não terminais são nomes de regras, como `file`, `statement`, `assignment`,
`expression`, `sum`, `term`, `factor` e `atom`. Eles organizam a estrutura, mas
não aparecem literalmente no programa.

## 7. Conferência com o Python

O módulo `ast` do Python representa a expressão de forma equivalente:

```text
Assign(
  targets=[Name(id='total')],
  value=BinOp(
    left=Constant(value=2),
    op=Add(),
    right=BinOp(
      left=Constant(value=3),
      op=Mult(),
      right=Constant(value=4))))
```

O nó da multiplicação aparece como operando direito da soma, confirmando o
agrupamento `2 + (3 * 4)`.

## 8. Observação sobre PEG

Uma gramática livre de contexto tradicional costuma ser apresentada como um
mecanismo que gera sentenças. Uma PEG descreve um reconhecedor e suas escolhas
são ordenadas. Nesta atividade, a seta `⇒` foi usada de modo didático para
mostrar o caminho das regras até os tokens reconhecidos.

## Referências

- [Python - especificação completa da gramática](https://docs.python.org/3/reference/grammar.html)
- [Python - análise léxica](https://docs.python.org/3/reference/lexical_analysis.html)
- [PEP 617 - novo analisador PEG do CPython](https://peps.python.org/pep-0617/)
- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11. ed.
  Capítulo 3: descrição da sintaxe e da semântica.
