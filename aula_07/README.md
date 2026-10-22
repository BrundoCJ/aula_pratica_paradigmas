# Atividade - Aula 07

[← Voltar ao índice](../README.md)

Exercício **"encontre o bug"** sobre **expressões, atribuição e estruturas de
controle**, com base nos capítulos 7 e 8 de *Conceitos de Linguagens de
Programação*, de Robert W. Sebesta.

Para cada trecho: **(a)** qual é a saída? **(b)** qual regra causa o problema?
**(c)** como corrigir?

| # | Linguagem | Saída | Regra |
|---|---|---|---|
| 1 | JavaScript | `Total: 0012` | `for...in` percorre chaves (strings) |
| 2 | Python | `180.0` | `0` é falso em `or` |
| 3 | Java | `inválido` | *fall-through* no `switch` |
| 4 | C | `saldo insuficiente` e `fim` | `;` vazio depois do `if` |
| 5 | Go | `dentro: 20` e `fora: 10` | `:=` cria nova variável (ocultação) |
| 6 | Java | `0.0%` | divisão inteira |

## 1 · JavaScript

```javascript
const precos = [10, 20, 30];
let total = 0;
for (const p in precos) total += p;
console.log("Total: " + total);
```

**(a) Saída**

```text
Total: 0012
```

**(b) Regra: `for...in` percorre as chaves, não os valores, e `+` com string concatena**

Em um array, `for...in` devolve os índices como **strings**: `"0"`, `"1"` e
`"2"`. Na primeira volta, `0 + "0"` sofre coerção e vira a string `"00"`. Daí
em diante, `+=` só concatena: `"001"`, `"0012"`.

**(c) Correção**

```javascript
for (const p of precos) total += p;
console.log("Total: " + total); // Total: 60
```

## 2 · Python

```python
def desconto(preco, d=None):
    d = d or 10     # padrão: 10%
    return preco * (100 - d) / 100

print(desconto(200, 0))
```

**(a) Saída**

```text
180.0
```

**(b) Regra: "truthiness" e curto-circuito do `or`**

`a or b` devolve `a` se ele for verdadeiro e `b` caso contrário. Em Python, `0`
é falso, assim como `None`. Por isso, um desconto de `0` explícito é trocado
pelo padrão `10`, e o resultado é 180 em vez de 200.

**(c) Correção**

```python
def desconto(preco, d=None):
    if d is None:
        d = 10
    return preco * (100 - d) / 100

print(desconto(200, 0))  # 200.0
```

## 3 · Java

```java
int dia = 2;
String nome = "";
switch (dia) {
    case 1: nome = "domingo";
    case 2: nome = "segunda";
    case 3: nome = "terça";
    default: nome = "inválido";
}
System.out.println(nome);
```

**(a) Saída**

```text
inválido
```

**(b) Regra: sem `break`, o controle "cai" para os casos seguintes**

O `switch` herdado de C desvia para `case 2` e continua executando todos os
casos abaixo (*fall-through*). `nome` recebe `"segunda"`, depois `"terça"` e
por fim `"inválido"`.

**(c) Correção**

```java
switch (dia) {
    case 1 -> nome = "domingo";
    case 2 -> nome = "segunda";
    case 3 -> nome = "terça";
    default -> nome = "inválido";
}
```

A sintaxe com `->` (Java 14+) não tem *fall-through*. Na sintaxe antiga, basta
colocar `break;` no fim de cada caso.

## 4 · C

```c
int saldo = 100, saque = 50;
if (saque > saldo);
    printf("saldo insuficiente\n");
printf("fim\n");
```

**(a) Saída**

```text
saldo insuficiente
fim
```

**(b) Regra: o `;` logo após o `if` é uma sentença vazia**

O corpo do `if` é a sentença vazia `;`. O `printf` seguinte não faz parte do
`if` e sempre executa. A endentação engana o leitor, mas não muda nada para o
compilador.

**(c) Correção**

```c
if (saque > saldo) {
    printf("saldo insuficiente\n");
}
printf("fim\n");
```

Usar chaves sempre evita esse erro e o do "else pendente".

## 5 · Go

```go
x := 10
if x > 5 {
    x := x * 2
    fmt.Println("dentro:", x)
}
fmt.Println("fora:", x)
```

**(a) Saída**

```text
dentro: 20
fora: 10
```

**(b) Regra: `:=` declara uma nova variável no bloco interno**

Dentro do `if`, `x := x * 2` cria um **novo** `x`, local ao bloco, que oculta o
`x` externo. O lado direito ainda lê o `x` de fora (10). Ao sair do bloco, o
`x` interno deixa de existir e o externo continua valendo 10.

**(c) Correção**

```go
if x > 5 {
    x = x * 2
    fmt.Println("dentro:", x)
}
fmt.Println("fora:", x) // fora: 20
```

## 6 · Java

```java
int acertos = 7, total = 10;
double taxa = acertos / total * 100;
System.out.println(taxa + "%");
```

**(a) Saída**

```text
0.0%
```

**(b) Regra: o tipo da operação é decidido pelos operandos, não pelo destino**

`acertos / total` é uma divisão entre `int`, então `7 / 10` dá `0`. Depois,
`0 * 100` dá `0`. Só então ocorre o alargamento para `double` na atribuição,
quando a informação já se perdeu.

**(c) Correção**

```java
double taxa = (double) acertos / total * 100;
System.out.println(taxa + "%"); // 70.0%
```

O *cast* converte `acertos` antes da divisão, que passa a ser de ponto
flutuante.

## Referência

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11. ed.
  Capítulos 7 e 8: expressões, atribuição e estruturas de controle.
