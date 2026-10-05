# Exercício: qual é a saída? (2/3)

Para cada trecho: **(a)** qual é a saída? **(b)** qual conceito da aula explica?

## 3 · Python

```python
fs = [lambda: i for i in range(3)]
print([f() for f in fs])
```

**(a) Saída**

```text
[2, 2, 2]
```

**(b) Conceito: *closures* capturam a variável, não o valor (vinculação tardia)**

Cada `lambda` é uma *closure* que guarda uma referência à **variável** `i` do
escopo da compreensão de lista, e não uma cópia do valor que `i` tinha quando
a `lambda` foi criada. As três funções compartilham a mesma variável. Quando
elas são chamadas, o laço já terminou e `i` vale `2`, então todas retornam `2`.

Para capturar o valor no momento da criação, use um parâmetro com valor
padrão, que é avaliado na definição:

```python
fs = [lambda i=i: i for i in range(3)]
print([f() for f in fs])  # [0, 1, 2]
```

## 4 · C

```c
int contador(void) {
    static int n = 0;
    return ++n;
}
// em main:
contador(); contador();
printf("%d\n", contador());
```

**(a) Saída**

```text
3
```

**(b) Conceito: variável local estática, escopo diferente de tempo de vida**

`static` dá a `n` **tempo de vida estático**: a variável é alocada e
inicializada uma única vez, antes da execução, e mantém o valor entre as
chamadas. O **escopo** continua local, ou seja, só `contador` enxerga `n`.

As chamadas produzem `1`, `2` e `3`. Só a terceira é impressa.

Sem `static`, `n` seria uma variável dinâmica de pilha, recriada com `0` a
cada chamada, e a saída seria `1`.
