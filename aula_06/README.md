# Atividade - Aula 06

[← Voltar ao índice](../README.md)

Exercício **"preveja a saída"** sobre **tipos de dados**, com base no capítulo 6
de *Conceitos de Linguagens de Programação*, de Robert W. Sebesta.

Para cada trecho: **(a)** qual é a saída? **(b)** o problema é detectado na
compilação, na execução ou nunca?

| # | Linguagem | Saída | Detecção |
|---|---|---|---|
| 1 | JavaScript | `false` e `9007199254740992` | nunca |
| 2 | Python | `4 5` | não há erro |
| 3 | Go | `0` | nunca |
| 4 | Java | `0` e depois `ArrayIndexOutOfBoundsException` | execução |
| 5 | Rust | não compila (E0382) | compilação |
| 6 | C | `1065353216` | nunca |

## 1 · JavaScript

```javascript
console.log(0.1 * 3 === 0.3);
console.log(9007199254740993);
```

**(a) Saída**

```text
false
9007199254740992
```

**(b) Detecção: nunca. Conceito: ponto flutuante IEEE 754**

`Number` em JavaScript é um `double` de 64 bits. `0,1` é uma dízima em binário,
então `0.1 * 3` vale `0.30000000000000004` e a comparação com `0.3` dá `false`.

A mantissa tem 53 bits, então só os inteiros até 2⁵³ (`9007199254740992`) são
representados todos com exatidão. `9007199254740993` não cabe e é arredondado
para o vizinho representável. Nenhum aviso é emitido.

Correção: comparar com tolerância (`Math.abs(a - b) < Number.EPSILON`) e usar
`BigInt` (`9007199254740993n`) para inteiros grandes.

## 2 · Python

```python
palavra = "maçã"
print(len(palavra), len(palavra.encode()))
```

**(a) Saída**

```text
4 5
```

**(b) Detecção: não há erro. Conceito: caracteres × bytes (Unicode e UTF-8)**

Em Python, `str` é uma sequência de caracteres Unicode, então `len` conta 4
caracteres. `encode()` gera os bytes em UTF-8: `m` e `a` ocupam 1 byte cada,
`ç` e `ã` ocupam 2 bytes cada, somando 5.

O "tamanho" de uma cadeia depende do que se conta. Isso importa ao limitar
campos em bytes, como em bancos de dados e protocolos de rede.

## 3 · Go

```go
var b byte = 255
b++
fmt.Println(b)
```

**(a) Saída**

```text
0
```

**(b) Detecção: nunca. Conceito: estouro de inteiro sem sinal**

`byte` é um apelido de `uint8`, inteiro sem sinal de 8 bits (0 a 255). Somar 1
a 255 dá a volta, por aritmética módulo 2⁸, e o resultado é 0. Go não verifica
estouro em tempo de execução para inteiros.

Rust, em modo debug, geraria *panic* nesse caso. Java não tem tipos sem sinal.

## 4 · Java

```java
int[] v = new int[3];
System.out.println(v[0]);
System.out.println(v[3]);
```

**(a) Saída**

```text
0
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3
```

**(b) Detecção: execução. Conceito: verificação de índices**

Java inicializa os elementos de um array numérico com `0`, então `v[0]` imprime
`0`. Os índices válidos vão de 0 a 2. Java verifica cada acesso contra a faixa
e lança exceção em `v[3]`.

Em C, o mesmo acesso não seria verificado: leria lixo da memória sem aviso.

## 5 · Rust

```rust
let s = String::from("oi");
let t = s;
println!("{} {}", s, t);
```

**(a) Saída**

Não há saída: o programa **não compila**.

```text
error[E0382]: borrow of moved value: `s`
```

**(b) Detecção: compilação. Conceito: *ownership* e semântica de movimento**

`String` guarda dados no *heap* e não implementa `Copy`. `let t = s` **move** a
posse do valor para `t`, e `s` deixa de ser válido. O compilador rejeita o uso
de `s` no `println!`, evitando dois donos para a mesma memória.

Correção: `let t = s.clone();` para ter duas cópias, ou `let t = &s;` para só
emprestar.

## 6 · C

```c
union { int i; float f; } u;
u.f = 1.0f;
printf("%d\n", u.i);
```

**(a) Saída**

```text
1065353216
```

**(b) Detecção: nunca. Conceito: união livre**

Os campos de uma união compartilham a mesma memória. O programa grava um
`float` e lê os mesmos 4 bytes como `int`. Em IEEE 754, `1.0f` é `0x3F800000`,
que como inteiro vale `1065353216`.

C não guarda qual campo está ativo (união livre, sem discriminante), então não
há verificação de tipo. Rust e TypeScript usam uniões discriminadas, em que o
compilador obriga a testar qual variante está presente.

## Referência

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11. ed.
  Capítulo 6: tipos de dados.
