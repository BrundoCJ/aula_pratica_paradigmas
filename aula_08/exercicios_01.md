# Exercício: qual é a saída? (1/3)

Para cada trecho: **(a)** qual é a saída? **(b)** qual conceito da aula explica?

## 1 · Python

```python
def adicionar(item, lista=[]):
    lista.append(item)
    return lista

print(adicionar(1))
print(adicionar(2))
```

**(a) Saída**

```text
[1]
[1, 2]
```

**(b) Conceito: momento de vinculação (*binding time*) e tempo de vida do valor padrão**

O valor padrão `[]` é avaliado **uma única vez**, quando o `def` é executado,
e não a cada chamada. A lista criada nesse momento fica vinculada à função e
vive enquanto a função existir. Como listas são mutáveis, todas as chamadas
que omitem `lista` compartilham o mesmo objeto, e o `append` da primeira
chamada continua visível na segunda.

Forma correta:

```python
def adicionar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

## 2 · Java

```java
static void zera(int[] v, int n) {
    v[0] = 0;
    n = 0;
}
int[] v = {5, 5}; int n = 5;
zera(v, n);
System.out.println(v[0] + " " + n);
```

**(a) Saída**

```text
0 5
```

**(b) Conceito: passagem de parâmetros por valor e *aliasing***

Java sempre passa parâmetros **por valor**:

- `n` é um `int` primitivo; o método recebe uma cópia, então `n = 0` altera só
  a cópia local e o `n` do chamador continua `5`.
- `v` é uma referência para um array; o método recebe uma cópia **da
  referência**, que aponta para o mesmo array. O parâmetro e a variável do
  chamador são *aliases* do mesmo objeto, por isso `v[0] = 0` é visível fora.

Se o método fizesse `v = new int[]{9, 9};`, o chamador não veria a troca,
porque só a cópia da referência seria alterada.
